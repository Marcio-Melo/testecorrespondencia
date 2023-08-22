import os
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver

# URL do site oficial do Chromedriver
chromedriver_url = "https://googlechromelabs.github.io/chrome-for-testing/"

# Função para obter a versão atual do Chrome instalada no sistema
def get_current_chrome_version():
    chrome_exe_path = "D:\\Users\\marcio.melo\\Desktop\\chrome.exe"  # Caminho para o executável do Chrome #D:\\Users\\marcio.melo\\Desktop\\chrome.exe
    version_info = os.popen(f'"{chrome_exe_path}" --version').read()
    version = version_info.split()[2]
    return version

# Função para obter a versão mais recente do Chromedriver do site oficial
def get_latest_chromedriver_version():
    response = requests.get(chromedriver_url)
    soup = BeautifulSoup(response.text, "html.parser")
    download_links = soup.find_all("a", href=True)
    
    for link in download_links:
        if "win32" in link["href"] and "64" in link["href"]:
            version = link["href"].split("/")[-2]
            return version

# Função para baixar e substituir o Chromedriver antigo
def update_chromedriver():
    current_chrome_version = get_current_chrome_version()
    latest_chromedriver_version = get_latest_chromedriver_version()
    
    if latest_chromedriver_version != current_chrome_version:
        chromedriver_download_url = f"{chromedriver_url}{latest_chromedriver_version}/chromedriver_win32.zip"
        response = requests.get(chromedriver_download_url)
        
        with open("chromedriver_win32.zip", "wb") as f:
            f.write(response.content)
            
        # Extrair o arquivo ZIP e substituir o Chromedriver antigo
        # ... (coloque aqui o código para extrair e substituir)
        
        print("Chromedriver atualizado com sucesso!")
    else:
        print("Chromedriver já está atualizado.")

# Executar a função de atualização do Chromedriver
update_chromedriver()
