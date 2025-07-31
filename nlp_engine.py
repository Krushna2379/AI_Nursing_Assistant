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

