# Pay attention to check that your OpenAI version must be v0.27.0 or above
import openai
import re
from queryPinecone import vectorSearch
from colorama import Fore, Style
# First, you need to set up your API key
openai.api_key = "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"
# Then, you can call the "gpt-3.5-turbo" model
model_engine = "gpt-3.5-turbo-16k-0613"

messages=[
{"role": "system", "content": "You are a friendly AI sales assistant"},
{"role": "user", "content": """You are an AI sales assistant. Your task is to assist customers by recommending products. 
When asked about a product or product recommendation, you will explicitly look up the relevant products in the database. You won't recommend products
based on your training data but based on the information retrieved from the database. Before you recommend a product you must ask about any allergies or prefrences, and you will use these in your search. To search the database, you will enclose your query within {SEARCH}.
All queries must be made at the end of your message, and multiple queries are allowed as long as they are individually wrapped in {SEARCH}. You can query for specific products or types of products.
Here's an example:

USER: Hi, I'm looking for a three step skin care routine.

ASSISTANT: Sure, I would love to assist you! Do you have any specific allergies or prefrences I should know of?

USER: Yes, I have dry sensitive skin

ASSISTANT: Sure, I can help with that. I am looking for the best products for you now. {SEARCH}clenser for dry sensitive skin{SEARCH} {SEARCH}serum for dry sensitive skin{SEARCH} {SEARCH}moisturizer for dry sensitive skin{SEARCH}

Then I will respond with the product details.
Please note, you should only recommend products that you find from the database. Do not invent new products or use products you already know of.

Once you recommend a product from the database you must provide the product link or links if its multiple products at the end of your message enclosed by [here]() with the link in the parentheses. This is because I am going to display cards with images and the link to the product at the end of your message. you can continue to discuss that product in following messages without providing the link each time. However, you need to end your message after making a database query.

Also, remember to always greet customers in a friendly manner. Let's practice.
"""},
{"role":"assistant", "content": "Hello! Welcome to Origins AI Experience, how may I assist you? "}
]

# Enter a while loop
while True:
    # Get user input
    input_text = input("User: ")

    # Append user's input to the messages
    messages.append({"role": "user", "content": input_text})

    # Send an API request with the updated messages list
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages,
        temperature=0.7
    )

    # Parse the response and output the result
    output_text = response['choices'][0]['message']['content']
    print(Fore.GREEN + output_text)
    print(Style.RESET_ALL)
    # Append assistant's response to the messages
    messages.append({"role": "assistant", "content": output_text})

    # Search for queries within &&
    queries = re.findall('{SEARCH}(.*?){SEARCH}', output_text)
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
        products = re.findall('\]\((.*?)\)', output_text)
        print("PRODUCTS: ", products)
        print(Fore.GREEN + output_text)
        print(Style.RESET_ALL)
        # Append assistant's response to the messages
        messages.append({"role": "assistant", "content": output_text})