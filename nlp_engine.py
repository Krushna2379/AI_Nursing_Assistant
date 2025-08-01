import os
from openai import OpenAI

# Create client with API key
client = OpenAI(api_key="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")

def get_ai_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI nurse assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

