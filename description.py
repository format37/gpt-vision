from openai import OpenAI
import json

def append_message(messages, role, text, image_url, detail):
    messages.append(
        {
            "role": role,
            "content": [
                {"type": "text", "text": text},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url,
                        "detail": detail
                    },
                },
            ],
        }
    )


def main()
    # Read openai api key from config.json
    with open("config.json") as f:
        data = json.load(f)
    api_key = data["api_key"].strip()
    model = data["model"]
    client = OpenAI(api_key = api_key)

    text = "Please, solve these equations and tell me what the difference between them."
    messages = []

    image_url = "https://github.com/format37/gpt-vision/blob/f93753c1f7cd88597839804be2aa564295535cc3/sample.jpg?raw=true"
    append_message(
        messages, 
        "user",
        text,
        image_url,
        "high"
    )

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=2000,
    )

    print(response.choices[0])
