import pyautogui
import pyperclip

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

navegador.get("https://sig.tse.jus.br/ords/mddsv/r/seai/sig-eleicao/estatisticas-eleicao?session=22422611165310")

# navegador.fullscreen_window

# navegador.find_element('xpath', '//*[@id="R374993496085821665_Cards"]/div/div[3]/ul/li[1]/div/a')

navegador.find_element('xpath', '/html/body/form/div[1]/div[2]/div[2]/main/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div[3]/ul/li[1]/div/a').click()

navegador.find_element('xpath', '/html/body/form/div[1]/div[2]/div[2]/main/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div[3]/ul/li[1]/div/a').click()

navegador.find_element('xpath', '/html/body/form/div[1]/div[2]/div[2]/main/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button[1]/span[2]').click()

print('Fim do teste')
texto = f"""
Texto fica formatado
caracteres especiais maçã, titã, olá
texto pegar varíaveis
R${total_gasto:,.2f}

Independente da quantidade de linhas.

"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

"""
pyautogui.click
pyautogui.write("escrever qualquer coisa]")
pyautogui.press("tab") #aperta somente uma tecla
pyautogui.hotkey("ctrl", "v") #para atalho
"""
# passos manuais para realizar este processo?
# 1 - Clicar e digitar meu usuário
# pyautogui.click(874, 26)
# pyautogui.click(1012, 541)