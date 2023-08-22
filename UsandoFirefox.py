from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

servico = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=servico)


## Usando Geckdriver
navegador.maximize_window()

navegador.get("https://sig.tse.jus.br/ords/mddsv/r/seai/sig-eleicao/estatisticas-eleicao?session=22422611165310")

# navegador.fullscreen_window

# navegador.find_element('xpath', '//*[@id="R374993496085821665_Cards"]/div/div[3]/ul/li[1]/div/a')

navegador.find_element('xpath', '/html/body/form/div[1]/div[2]/div[2]/main/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div[3]/ul/li[1]/div/a').click()

navegador.find_element('xpath', '/html/body/form/div[1]/div[2]/div[2]/main/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div[3]/ul/li[1]/div/a').click()

valor = navegador.find_element('xpath', '/html/body/form/div[1]/div[2]/div[2]/main/div[2]/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div/div/div[3]/div/div[3]/ul/li/div/div[2]/div').get_attribute('div class')

print(valor)
#navegador.find_element('xpath', '/html/body/form/div[1]/div[2]/div[2]/main/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button[1]/span[2]').click()

print('Fim do teste')