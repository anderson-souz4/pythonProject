# README

## Introdução

Este é um bot para WhatsApp, escrito em Python, que utiliza a API da OpenAI para responder a perguntas e realizar conversas. Para utilizar este bot, você precisará instalar as dependências necessárias, bem como obter uma chave API da OpenAI.

## Instalação

Para utilizar este bot, siga as etapas abaixo:

1. Instale o pacote `pipe` usando o pip:
   ```
   pip install pipe
   ```

2. Instale as dependências do bot a partir do arquivo `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

3. Crie uma conta na OpenAI e obtenha uma chave API.

4. Defina a variável de ambiente `OPENAI_API_KEY` com a chave API obtida:
   ```
   export OPENAI_API_KEY=<sua chave API>
   ```

5. Inicie o bot:
   ```
   python bot.py
   ```

## Uso

Após iniciar o bot, você poderá se comunicar com ele por meio do WhatsApp. Para isso, adicione o número de telefone do bot à sua lista de contatos do WhatsApp e envie uma mensagem para ele.

O bot é capaz de responder a perguntas e realizar conversas. Para iniciar uma conversa, digite `iniciar conversa`. O bot responderá com uma saudação e aguardará sua mensagem. A partir daí, você pode digitar o que quiser e o bot tentará responder de forma coerente.

Para fazer uma pergunta ao bot, digite `pergunta:` seguido da sua pergunta. O bot utilizará a API da OpenAI para responder à sua pergunta.

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Todas as contribuições são bem-vindas!

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.