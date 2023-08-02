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
                    "details": product['Details'],
                }

        # Return None if no matching product is found
        return None

def vectorSearch(queries):
    AllResult = ""
    number_of_products = len(queries) * 2
    #print("\n\n\n\n\nproduct number :",number_of_products,"\n\n\n\n\n")
    messages=[{"role": "system", "content":f"""You are an AI Assistant. You will recieve a detailed JSON string with product data of ({number_of_products}) products and 
    summarize it in a short readable way for both products. Only output the name, price, a summary of the details, the key ingredients, a link to the product"""
    }]
    for query in queries:
        #print("QUERY\n",query,"\n")
        result = vectorstore.similarity_search(query, 2)
        
        for product in result:
            messages.append({"role": "assistant", "content": "[DATABASE] " + product.page_content + " [DATABASE]"})
       
    #print("\nALLRESULT\n", AllResult, "\n\nALLRESULT\n")
    
    # search_result =  vectorstore.similarity_search(query, 2)

    # for result in search_result:
    #     messages.append({"role": "user", "content": "[DATABASE] " + result.page_content + " [DATABASE]"})

    smartSearch = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages
    )
    summary = smartSearch['choices'][0]['message']['content']
    #print("\n\n SUMMARY \n",summary,"\nSUMMARY\n")
    return(summary)
