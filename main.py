import os
import openai

openai.api_key = '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'

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Crie uma função em postgres que retorne o nome do cliente e o valor total de suas compras.",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
resposta = response['choices'][0]['text']
print(resposta)
