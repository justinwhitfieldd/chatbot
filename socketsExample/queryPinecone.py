import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import os
import openai
import re
import json
from GPTresponse import OpenAIKey
# initialize pinecone
pinecone.init(
    api_key="28fc5376-0f64-4593-b629-aa5d98649225", 
    environment="us-west4-gcp-free"
)
index = pinecone.Index("products")

messages=[{"role": "system", "content":"""You are an AI Assistant. You will recieve verbose product data of two products and 
summarize it in a readable way for both products. Only output the name, price, a summary of the details, the key ingredients, a link to the product, and the image link"""
}]

embed = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=OpenAIKey
    )

text_field = "text"
vectorstore = Pinecone(
    index, embed.embed_query, text_field
    )

def get_product_info(productlink):
        # Load data from JSON file
        with open('productdetails.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        # Loop through the data to find the desired product
        for product in data:
            if product['ProductLink'] == productlink:
                return {
                    "link": product['ProductLink'],
                    "image": product['ImageLink'],
                    "name": product['Name'],
                    "price": product['Price'],
                }

        # Return None if no matching product is found
        return None

def vectorSearch(query):
    search_result =  vectorstore.similarity_search(query, 2)

    for result in search_result:
        messages.append({"role": "user", "content": "[DATABASE] " + result.page_content + " [DATABASE]"})

    smartSearch = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages
    )
    summary = smartSearch['choices'][0]['message']['content']
    return(summary)
