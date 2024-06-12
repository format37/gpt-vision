import json
from io import BytesIO
from PIL import Image
from openai import OpenAI
import openai
from PIL import Image
import requests

def convert_jpg_to_png(jpg_path, png_path):
    try:
        # Open the JPEG image
        image = Image.open(jpg_path)
        
        # Convert the image to RGB mode (if needed)
        image = image.convert("RGB")
        
        # Save the image as PNG
        image.save(png_path, "PNG")
        
        print(f"Image converted and saved as {png_path}")
    except IOError:
        print(f"Error: Unable to open or save the image.")

with open("config.json") as f:
    data = json.load(f)
    api_key = data["api_key"].strip()
    if api_key == "":
        raise ValueError("API key is empty")
    client = OpenAI(api_key = api_key)
    print("Openai client initialized. Sending request...")

# convert_jpg_to_png("input.jpg", "input.png")

response = client.images.create_variation(
  image=open("input.png", "rb"),
  n=1,
  model="dall-e-2",
  size="1024x1024"
)
# print url
print(response.data[0].url)
print("Image variation created. Downloading image...")
# Download image using requests
image = requests.get(response.data[0].url)
# Save image to file
with open("output.png", "wb") as file:
    file.write(image.content)
print("Image downloaded and saved as output.png")
