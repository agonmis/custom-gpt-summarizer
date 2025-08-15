from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def callOpenAI(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Du bist ein exzellenter Textzusammenfasser. Fasse den gegebenen Text in 1-2 Sätzen zusammen."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

