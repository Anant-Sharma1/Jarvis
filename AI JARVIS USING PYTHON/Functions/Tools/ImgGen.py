import asyncio
import requests
from random import randint
from os import startfile

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": "Bearer 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"}


async def query(payload):
	print("posting")
	response = await asyncio.to_thread(requests.post, API_URL, headers=headers, json=payload)
	return response.content

async def generate_images(prompt:str):
	tasks = []
	payload = {
		"inputs": f"{prompt} seed=15",
	}
	task = asyncio.create_task(query(payload))
	tasks.append(task)



	image_bytes_list = await asyncio.gather(*tasks)

	for i, image_bytes in enumerate(image_bytes_list):
		with open(f"output//image.jpg","wb") as f:
			f.write(image_bytes)
		startfile("output\\image.jpg")

def Generate_Images(prompt:str):
	asyncio.run(generate_images(prompt))

if __name__ == "__main__":
	Generate_Images("astronaut riding a horse")
     