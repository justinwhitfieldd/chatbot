#some dependencys unnecessary
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os
from langchain.llms import OpenAI
import openai
from langchain.document_loaders import UnstructuredFileLoader

with open('fakeproducts.txt') as f:
    products = f.read()
text_splitter = CharacterTextSplitter(        
    separator = "\n\n",
    chunk_size = 500,
    chunk_overlap  = 100,
    length_function = len,
)
texts = text_splitter.create_documents([products])

# uncomment to preview how the text was split
# for text in texts:
#     print(text)
#     print("\n")

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', "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")
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', "28fc5376-0f64-4593-b629-aa5d98649225")
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV', "us-west4-gcp-free")

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# initialize pinecone
pinecone.init(
    api_key="28fc5376-0f64-4593-b629-aa5d98649225",  # find at app.pinecone.io
    environment="us-west4-gcp-free"  # next to api key in console
)
index_name = "fakeproducts" # put in the name of your pinecone index here

docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)

#query example
query = "What products can I use that have ingredients salt?"
docs = docsearch.similarity_search(query)
print(docs[0].page_content)

