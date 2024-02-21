import base64
import requests
import json

# Read openai api key from config.json
with open("config.json") as f:
    data = json.load(f)
api_key = data["api_key"].strip()
model = data["model"]

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "sample.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": model,
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Пожалуйста, опишите максимально детально, что вы видите на этом изображении?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())