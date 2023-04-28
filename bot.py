from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import openai

dir__path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir__path + "profile/zap")
driver = webdriver.Chrome(chrome_options=chrome_options2)
driver.get('https://web.whatsapp.com/')
agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
#####API para pegar dados do whatsapp
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/SCxhCbBkAtiwg4ydWYXGO73ERox1yfag", headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
####
time.sleep(10)


def bot():
    try:
        ######Clica na bolinha de notificação
        bolinha = driver.find_elements(By.CLASS_NAME, bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
        clique_duplo(acao_bolinha)

        #### LER A MENSAGEM DO CLIENTE
        todas_as_mensagens = driver.find_elements(By.CLASS_NAME, msg_cliente)
        todas_as_mensagens_texto = [e.text for e in todas_as_mensagens]
        ultima_msg = todas_as_mensagens_texto[-1]
        print(ultima_msg)

        cliente = 'mensagem do cliente:'
        texto2 = 'Responda a mensagem do cliente com base no proximo texto:'
        # texto3 = 'Cardapio : 1 - Sopa de Letrinha, 2 - Strogonoff de frango'
        questao = cliente + ultima_msg + texto2

        #### processa a mensagem da api
        openai.api_key = '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'

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=questao,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        resposta = response['choices'][0]['text']
        print(resposta)
        time.sleep(3)

        ##RESPONDE A MENSAGEM
        campo_de_texto = driver.find_element(By.XPATH, caixa_msg)
        campo_de_texto.click()
        time.sleep(3)
        campo_de_texto.send_keys(resposta, Keys.ENTER)
        time.sleep(2)


        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()





    except:
        print('Buscando notificações...')
        time.sleep(1)


def clique_duplo(acao_bolinha):
    acao_bolinha.click()
    acao_bolinha.perform()
    acao_bolinha.click()
    acao_bolinha.perform()


while True:
    bot()
