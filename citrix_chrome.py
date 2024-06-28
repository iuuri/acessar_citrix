from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import getpass

# Função para obter dados de login do usuário
def obter_dados_login():
    usuario = input("Digite seu usuário: ")
    senha = getpass.getpass("Digite sua senha: ")
    autenticador = input("Digite seu código do autenticador: ")
    return usuario, senha, autenticador

# Obter dados de login
usuario, senha, autenticador = obter_dados_login()

# Configuração do WebDriver Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL do site
url_site = 'https://acessovdi.jbs.com.br/'

# Acessa o site
driver.get(url_site)

# Tempo máximo de espera para encontrar os elementos (em segundos)
tempo_espera = 10

try:
    # Espera até que o campo de usuário esteja presente
    campo_usuario = WebDriverWait(driver, tempo_espera).until(
        EC.presence_of_element_located((By.ID, 'login'))
    )
    campo_usuario.send_keys(usuario)

    # Espera até que o campo de senha esteja presente
    campo_senha = WebDriverWait(driver, tempo_espera).until(
        EC.presence_of_element_located((By.ID, 'passwd'))
    )
    campo_senha.send_keys(senha)

    # Espera até que o campo de autenticador esteja presente
    campo_autenticador = WebDriverWait(driver, tempo_espera).until(
        EC.presence_of_element_located((By.ID, 'passwd1'))
    )
    campo_autenticador.send_keys(autenticador)

    # Localiza e clica no botão de login
    botao_login = WebDriverWait(driver, tempo_espera).until(
        EC.element_to_be_clickable((By.ID, 'Logon'))
    )
    botao_login.click()

    # Loop para clicar no botão "OK" enquanto a caixa de mensagem estiver presente
    while True:
        try:
            # Verifica se a caixa de mensagem de erro está presente
            mensagem_erro = WebDriverWait(driver, tempo_espera).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'popup.messageBoxPopup.alert'))
            )
            if mensagem_erro:
                # Clica no botão "OK" para fechar a caixa de mensagem
                botao_ok = WebDriverWait(driver, tempo_espera).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'messageBoxAction'))
                )
                botao_ok.click()
        except:
            break  # Sai do loop quando a caixa de mensagem não estiver mais presente

    # Aguarda indefinidamente para inspecionar o resultado do login
    input("Pressione Enter para encerrar o script e fechar o navegador.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fecha o navegador
    driver.quit()
