#!/usr/bin/python3

import openai
import sys

api = "API_KEY_HERE"

args = sys.argv[1:]

question = ' '.join(args)

def skynet(q,z):
  openai.api_key = f"{z}"
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"{question}",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  print(response.choices[0].text)

def sarcasticmark(q,z):
  openai.api_key = f"{z}"
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"{question}",
    temperature=0.5,
    max_tokens=60,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0.0
  )
  print(response.choices[0].text)


if __name__ == "__main__":
    #sarcasticmarv(question, api)
    skynet(question, api)
