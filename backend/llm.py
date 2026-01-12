from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print(GEMINI_API_KEY)

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def recommend_best_deal(products):
    prompt = f"""
You are an AI shopping agent.

Product price data:
{products}

Tasks:
1. Identify the cheapest product
2. Compare prices across top shopping apps like amazon , flipkart etc . in table format
3. Recommend the best deal
4. Explain the reason simply
"""

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    full_response = ""
    for chunk in response:
        delta = chunk.choices[0].delta
        if delta and delta.content:
            full_response += delta.content

    return full_response
