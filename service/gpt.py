import os
from openai import OpenAI
from dotenv import load_dotenv,find_dotenv
import random

api_key = random.choice(os.environ.get("OPENAI_API_KEY").split(","))
client = OpenAI(api_key=api_key)

def init():
    global client
    _ = load_dotenv(find_dotenv())
    client.base_url = os.environ.get("OPENAI_BASE_URL")
    
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

import asyncio

def chat_with_gpt_stream(messages,model="moonshot-v1-8k",temperature=0.3):
    asyncio.run(estimate_token(messages,model))
    response = client.with_options(max_retries=3).chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=True
    )
    
    return response

def get_models():
    response = client.with_options(max_retries=3).models.list()
    return response

import requests
import json


async def estimate_token(message,model="moonshot-v1-8k",temperature=0.3):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(api_key),
    }

    data = {
        "model": model,
        "messages": message
    }

    response = requests.post('https://api.moonshot.cn/v1/tokenizers/estimate-token-count', headers=headers, data=json.dumps(data))

    print(response.json())
    
    return response
    
