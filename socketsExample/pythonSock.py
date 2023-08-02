from flask import Flask, render_template, session, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock
from GPTresponse import messages, products, OpenAIKey
import time
import openai
from queryPinecone import vectorSearch, get_product_info
import re

openai.api_key = OpenAIKey
model_engine = "gpt-3.5-turbo-16k-0613"

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'brnadtechrox' # This is supposed to be newly generated for each session but brand tech
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

@app.route('/')
def index():
    return render_template('index.html', async_mode=socket_.async_mode)


@socket_.on('my_event', namespace='/test')
def test_message(message):
    
    session['receive_count'] = session.get('receive_count', 0) + 1

    messages.append({"role": "user", "content": message['data']})
    
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages,
        temperature=0.5
    )

    # Parse the response and output the result
    output_text = response['choices'][0]['message']['content']

    # Search for queries within {SEARCH}
    queries = ""
    queries = re.findall('{SEARCH}(.*?){SEARCH}', output_text)
    # remove the search from the message to be outputted
    output_text = re.sub('{SEARCH}(.*?){SEARCH}',"", output_text)
    emit('my_response',
         {'data':output_text, 'count': session['receive_count']})
    # Append assistant's response to the messages
    messages.append({"role": "assistant", "content": output_text})

    print("QUERIES: ", queries)
    # If a query was made, add the search results to the messages and make another API call
    if queries:
        for query in queries:
            # Call the search function for each query found
            print("DATABASE QUERY: ", query)
            search_result = vectorSearch(query)
            #print("SEARCH RESULT :",search_result)
            # Add the database search result to the messages list
            messages.append({"role": "assistant", "content": "[DATABASE] " + search_result + " [DATABASE]"})

        # Send an API request with the updated messages list
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=messages
        )
        # Parse the response and output the result
        output_text = response['choices'][0]['message']['content']

        #find product links in output
        links = re.findall('\]\((.*?)\)', output_text)
        if links:
            for link in links:
                new_product = get_product_info(link)
                products.append(new_product)
        #NEED TO SEND JSON HERE

        output_text =  re.sub('\]\((.*?)\)',"", output_text)
        output_text =  re.sub('\[',"", output_text)
        #output_text =  re.sub(r'(\d+)(\.)', r'\n\1\2', output_text) add new lines to numbers followed by . like 1. 2. 3.
        # Append assistant's response to the messages
        messages.append({"role": "assistant", "content": output_text})
        print("EMITTING RESPONSE | ",output_text)
        emit('my_response',
            {'data':output_text, 'count': session['receive_count'], 'product_data': products})
    
@socket_.on('disconnect_request', namespace='/test')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)


if __name__ == '__main__':
    socket_.run(app, debug=True)