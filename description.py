from openai import OpenAI
import json

# Read openai api key from config.json
with open("config.json") as f:
    data = json.load(f)
api_key = data["api_key"].strip()
model = data["model"]
client = OpenAI(api_key = api_key)

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Пожалуйста, опишите максимально детально, что вы видите на этом изображении?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://github.com/format37/gpt-vision/blob/f93753c1f7cd88597839804be2aa564295535cc3/sample.jpg?raw=true",
            "detail": "high"
          },
        },
      ],
    }
  ],
  max_tokens=1000,
)

print(response.choices[0])
