#!/usr/bin/python3

import openai
import sys

api = "API_KEY_HERE"
cmd = sys.argv[1]
args = sys.argv[2:]
question = " ".join(args)


def skynet(q, z):
    openai.api_key = f"{z}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{q}",
        temperature=0.0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    print(response.choices[0].text)


def imgcreate(q, z):
    openai.api_key = f"{z}"
    response = openai.Image.create(prompt=f"{q}", n=1, size="1024x1024")

    print(response.data)


def editgpt(q, z):
    openai.api_key = f"{z}"
    response = openai.Edit.create(
        model="text-davinci-edit-001",
        input=f"{q}",
        instruction="Fix the spelling mistakes",
    )
    print(response.choices[0].text)


if __name__ == "__main__":
    if cmd == "img":
        imgcreate(question, api)
    if cmd == "edit":
        editgpt(question, api)
    if cmd == "q":
        skynet(question, api)
