from pydantic import BaseModel, Field
from openai import OpenAI
import json
from typing import Literal, List, Union, Any

class Student(BaseModel):
    wearing_color: str
    hand: Literal["raised", "lowered"]

class School(BaseModel):
    scene_description: str
    participating_students: List[Student]

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


def main():
    # Read openai api key from config.json
    with open("config.json") as f:
        data = json.load(f)
    api_key = data["api_key"].strip()
    model = data["model"]
    client = OpenAI(api_key = api_key)

    text = "Please, solve these equations and tell me what the difference between them."
    messages = []

    image_url = 'https://github.com/format37/gpt-vision/blob/6bbcad3a08657515dd0f078fb58e4c852405d133/equation_a.jpg?raw=true'
    append_message(
        messages, 
        "user",
        text,
        image_url,
        "high"
    )
    # Can be added more images

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=2000,
        response_format=School
    )

    print(response.choices[0])


if __name__ == "__main__":
    main()
