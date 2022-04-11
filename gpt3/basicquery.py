from urllib import response
from click import prompt
import openai
from sympy import content

def gpt3(sometext):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=sometext,
            temperature=0.1,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )
    content=response.choices[0].text.split('\n')
    print(content)

query = 'what is openai'

response = gpt3(query)
print(response)