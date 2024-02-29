import os
from openai import OpenAI
from dotenv import load_dotenv,find_dotenv

client = OpenAI(api_key="")

def init():
    global client
    _ = load_dotenv(find_dotenv())
    client = OpenAI(
        # api_key=os.environ.get("OPENAI_API_KEY"),
        # base_url=os.environ.get("OPENAI_BASE_URL")
        
        api_key= "ghu_LEjjZ8Cde4rxST7n26rJstTYdeCxlu18BTxS"
        base_url="http://192.168.10.32:8848/v1"
    )
    
init()


def chat_with_gpt(message,model="gpt-3.5-turbo",temperature=0.5):
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

