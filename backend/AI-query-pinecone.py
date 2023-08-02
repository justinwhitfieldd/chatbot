from langchain.tools import BaseTool
from math import pi
from typing import Union
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import os
import pinecone
import time
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

pinecone.init(
    api_key="28fc5376-0f64-4593-b629-aa5d98649225",  # find at app.pinecone.io
    environment="us-west4-gcp-free"
)
index_name = 'fakeproducts'

index = pinecone.Index(index_name)
time.sleep(1)

class ProductSearch(BaseTool):
    name = "product search"
    description = "use this tool when you need to find relevant products, "

    def _run(self, query):
        OPENAI_API_KEY = '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'
        model_name = 'text-embedding-ada-002'
        embed = OpenAIEmbeddings(
            model=model_name,
            openai_api_key=OPENAI_API_KEY
        )

        text_field = "text"
        vectorstore = Pinecone(
            index, embed.embed_query, text_field
        )

        #query = "what is a product with crystals?"

        vectorstore.similarity_search(
            query,  # our search query
            k=3  # return 3 most relevant docs
        )

        # chatbot language model
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            model_name='gpt-3.5-turbo',
            temperature=0.0,
            verbose=True
        )
        # retrieval augmented pipeline for chatbot
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )
        return qa.run(query)
    
    def _arun(self, query):
        raise NotImplementedError("This tool does not support async")

OPENAI_API_KEY = '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'

# initialize LLM (we use ChatOpenAI because we'll later define a `chat` agent)
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.5,
    model_name='gpt-3.5-turbo'
)
# initialize conversational memory
conversation_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)
tools = [ProductSearch()]

# initialize agent with tools
agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=llm,
    verbose=False,
    max_iterations=4,
    early_stopping_method='generate',
    memory=conversation_memory,
    handle_parsing_errors=True,
)
sys_msg = """You are a very friendly sales assistant that sells fake products. You are very polite. You only want customers to buy products you recommend. Do not repeat your output. You can only recommend products you find in the database. Your goal is to sell products to customers. Before you recommend a product ask if the customer has any allergies and if so do not recommend products containing ingredients they are allergic to"""

new_prompt = agent.agent.create_prompt(
    system_message=sys_msg,
    tools=tools
)
agent.agent.llm_chain.prompt = new_prompt

print(agent.run("how are you doing today"))
print("\n")
print(agent.run("what are the ingredients in the Crystal Clear Body Lotion?"))
print("\n")
print(agent.run("What are some other lotions I might like?"))
print("\n")
print(agent.run("I do not like that one, could you recommend a different one instead"))
print("\n")
print(agent.run("What is a three step skin care routine I can start?"))