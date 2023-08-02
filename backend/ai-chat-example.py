import inspect
import agentpt2 as shit
from getpass import getpass
from langchain import OpenAI
from langchain.chains import LLMChain, ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory, 
                                                  ConversationSummaryMemory, 
                                                  ConversationBufferWindowMemory,
                                                  ConversationKGMemory)
from langchain.callbacks import get_openai_callback
import tiktoken
from langchain.chat_models import ChatOpenAI

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
messages = [
    SystemMessage(content="You are a skincare sales assistant.   ")
]
OPENAI_API_KEY = 'put_yo_key_here'

chat = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.2,
    model='gpt-3.5-turbo'
)

#res = chat(messages)

while True:
    res = chat(messages)
    print(res.content)
    messages.append(res)
    messages.append(HumanMessage(content=input()))
