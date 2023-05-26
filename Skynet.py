#!/usr/bin/python3

import openai
import sys

api = "INSERT API KEY"  # Not recommended to keep it here. Save using OpenAI builtin asset management function.
cmd = sys.argv[1]
args = sys.argv[2:]
question = " ".join(args)


def helperdocumentation():
    print("Available functions:")
    print(skynet.__doc__)
    print(editgpt.__doc__)
    print(imgcreate.__doc__)


def skynet(q, z):
    """Ask GPT-3 anything.
    use "query" followed by inquiry or question to query at GPT-3.
    Uses text-davinci-003 language model to fetch answers from, trained on 2021 content.
    """
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
    """Image creation.
    Use "img" followed by text description of image, to create an image using Dall-E".
    Uses dall-e language model to create images based on text.
    """
    openai.api_key = f"{z}"
    response = openai.Image.create(prompt=f"{q}", n=1, size="1024x1024")

    print(response.data)


def editgpt(q, z):
    """Text proofing.
    Use "edit" followed by text to proof any spelling mistakes.
    Uses text-davinci-edit-001 to correct any spelling mistakes.
    """
    openai.api_key = f"{z}"
    response = openai.Edit.create(
        model="text-davinci-edit-001",
        input=f"{q}",
        instruction="Fix the spelling mistakes",
    )
    print(response.choices[0].text)


if __name__ == "__main__":
    if cmd == "query":
        skynet(question, api)
    if cmd == "img":
        imgcreate(question, api)
    if cmd == "edit":
        editgpt(question, api)
    if cmd == "help":
        helperdocumentation()
