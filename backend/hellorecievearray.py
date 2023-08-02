from flask import Flask, render_template, send_from_directory, session
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from threading import Lock
import json
import openai
import re
from queryPinecone import vectorSearch, get_product_info
from GPTresponse import OpenAIKey
import time
import os

async_mode = None

# First, you need to set up your API key
openai.api_key = "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"
model_engine = "gpt-3.5-turbo-0613"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST"], allow_headers="*")
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()
@socketio.on('my_event', namespace='/test')

def test_message(message):
    prompt="""You are an AI sales assistant for the origins brand. All of your responses are very short. Your task is to assist customers by recommending products. 
    When asked about a product or product recommendation, you will explicitly look up the relevant products in the database. You won't recommend products
    based on your training data but based on the information retrieved from the database. Before you recommend a product you must ask about any allergies or prefrences, and you will use these in your search. Your next message after asking
    about allergies or prefrences must contain a product search. To search the database, you will enclose your query within {SEARCH}.
    All queries must be made at the end of your message, and multiple queries are allowed as long as they are individually wrapped in {SEARCH}. You can query for specific products or types of products.
    You must end your message after doing a query
    Here's an example:

    USER: Hi, I'm looking for a three step skin care routine.

    ASSISTANT: Sure, I would love to assist you! Do you have any specific allergies or prefrences I should know of?

    USER: Yes, I have dry sensitive skin

    ASSISTANT: Sure, I can help with that. I am looking for the best products for you now. {SEARCH}clenser for dry sensitive skin{SEARCH} {SEARCH}serum for dry sensitive skin{SEARCH} {SEARCH}moisturizer for dry sensitive skin{SEARCH}

    Then you will end your message.
    Please note, you must end your response after doing using {SEARCH}. Also you should only recommend products that you find from the database. Do not invent new products or use products you already know of.

    using {search} will return two products for each query. you do not have to recommend both, instead you must choose the product that best fits the customer's needs. Once you recommend a product from the database you must provide the product link or links 
    if its multiple products at the end of your message enclosed by [here]() with the link in the parentheses.Do not say it like "Find it here and here." This is because
     I am going to be parsing your response to find the product links and display cards with images and the link to the product at the end of your message. you can continue to discuss that product in following messages without providing the link each time. 
     However, you need to end your message after making a database query. Make sure you keep your messages short and simple and be very positive. Try to not exceed 30 words

    Information about Origins:
        Origins is committed to sustainability and environmental efforts. They prioritize sustainability in their ingredient selection, packaging design, manufacturing practices, and tree-planting initiatives. Since 2009, they have planted and cared for over 2.3 million trees in various locations worldwide. They source high-quality ingredients responsibly and work with a diverse network of suppliers, considering local communities. Moreover, Origins is dedicated to creating packaging that is recyclable, refillable, reusable, or made from recycled materials, and they prioritize using environmentally friendly materials for new store fixtures and visual merchandising.
    
    YOUR GOALS:
     1. Only recommend products found using {SEARCH}
     2. Provide short accurate responses
     3. Convince customer to purchase products
     4. Talk about Origin's green initiatives"""


    products=[]

    session['receive_count'] = session.get('receive_count', 0) + 1
    message.insert(0,{"role": "system", "content": prompt})
    #messages.append({"role": "user", "content": message['data']})
    
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=message,
        temperature=0.7
    )

    # Parse the response and output the result
    output_text = response['choices'][0]['message']['content']
    message.append({"role": "assistant", "content": output_text})
    # Search for queries wrapped in {SEARCH}
    queries = ""
    queries = re.findall('{SEARCH}(.*?){SEARCH}', output_text)
    #print(output_text)
    #print("QUERIES: ", queries)
    output_text = re.sub(r'\{SEARCH\}(.*?)\{SEARCH\}.*$', "", output_text)
    #output_text =  re.sub(r'(\d+)(\.)', "\\n", output_text)
    emit('my_response',
         {'data':output_text, 'count': session['receive_count'], 'products': products})

    # If a query was made, add the search results to the messages and make another API call
    if queries:
        result = ""
        all_results = vectorSearch(queries)
        # for query in queries:
        #     # Call the search function for each query found
        #     print("\n\nDATABASE QUERY: ", query)
        #     result = vectorSearch(query)
        #     print("\n\n Database query result: ", result)
        #     all_results = result
        #print("\n\nall result in main \n",all_results,"\n\nall result in main \n")
        # Add the database search result to the messages list
        message.append({"role": "assistant", "content": "[DATABASE] " + all_results + " [DATABASE]"})
        #print("\n\nmessage\n",message,"\n\nmessage")
        # Send an API request with the updated messages list
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=message
        )

        # Parse the response and output the result
        output_text = response['choices'][0]['message']['content']

        #find product links in output
        links = re.findall('\]\((.*?)\)', output_text)
        if links:
            for link in links:
                if link != "https://www.origins.com/":
                    #print("LINK: \n", link)
                    new_product = get_product_info(link)
                    products.append(new_product)
        #NEED TO SEND JSON HERE

        #remove link from output
        output_text =  re.sub('\]\((.*?)\)',"", output_text)
        output_text =  re.sub('\[',"", output_text)
        #output_text =  re.sub(r'(\d+)(\.)', r'\\n\1\2', output_text)
        #print("EMITTING RESPONSE | ",output_text)
        emit('my_response',
            {'data':output_text, 'count': session['receive_count'], 'products': products})

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('./static/', path)

@app.route('/_next/<path:path>')
def send_report(path):
    print(path)
    return send_from_directory('./static/_next', path)
if __name__ == '__main__':
    socketio.run(app, debug=True)
