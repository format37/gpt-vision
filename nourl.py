import base64
import requests
import json

def append_message(messages, role, text, image_url):
    messages.append(
        {
            "role": role,
            "content": [
                {"type": "text", "text": text},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                },
            ],
        }
    )

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def main():
    # Read openai api key from config.json
    with open("config.json") as f:
        data = json.load(f)
    api_key = data["api_key"].strip()
    model = data["model"]

    # text = "Пожалуйста, опишите максимально детально, что вы видите на этом изображении?"
    text = "Please, solve these equations and tell me what the difference between them."
    messages = []

    # Path to your image
    # image_path = "sample.jpg"
    image_path = "equation_a.jpg"
    base64_image = encode_image(image_path)
    image_url = f"data:image/jpeg;base64,{base64_image}"    
    append_message(
        messages, 
        "user",
        text,
        image_url
    )

    image_path = "equation_b.jpg"
    base64_image = encode_image(image_path)
    image_url = f"data:image/jpeg;base64,{base64_image}"    
    append_message(
        messages, 
        "user",
        text,
        image_url
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json={
            "model": model,
            "messages": messages,
            "max_tokens": 2000
        }
    )

    print(response.json())

if __name__ == "__main__":
    main()