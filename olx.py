import pyautogui
import requests

from bs4 import BeautifulSoup
from lxml import html
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
navegador.maximize_window()

# entra na página inicial da olx, e deve fazer login
navegador.get(
    "https://conta.olx.com.br/acesso?")
# preenche e-mail
navegador.find_element(
    'xpath', '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/div/span/input').send_keys("marciosystem10@gmail.com")

# preenche senha
navegador.find_element(
    'xpath', '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[2]/div/div/span/input').send_keys("Berserker04@")

#clica em entrar
navegador.find_element(
    'xpath', '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/button').click



"""
link = 'https://conta.olx.com.br/acesso?'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)
print(requisicao)
"""