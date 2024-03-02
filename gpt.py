import os
from openai import OpenAI
from dotenv import load_dotenv,find_dotenv
import random

client = OpenAI(api_key="")
key_pool = ["sk-G09Ep42Fkb7omJQ0tlfKmTM1r6uOi9EcZ1tmjtJ3wB9kEiz2","sk-qgaiYRcJ7JVF7V8Y8OSccOigDlDZf4b8KWVdHm606YtgPGqF"]
def init():
    global client
    _ = load_dotenv(find_dotenv())
    client = OpenAI(
        # api_key=os.environ.get("OPENAI_API_KEY"),
        
        api_key= random.choice(key_pool),
        base_url=os.environ.get("OPENAI_BASE_URL")
    )
    
init()


def chat_with_gpt(message,model="gpt-3.5-turbo",temperature=0.3):
    response = client.with_options(max_retries=3).chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=temperature,
    )
    return response

def chat_with_gpt_stream(message,model="moonshot-v1-8k",temperature=0.3):
    response = client.with_options(max_retries=3).chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=temperature,
        stream=True
    )
    
    return response