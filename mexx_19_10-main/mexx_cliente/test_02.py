import pytest
import time
from paginas.loginpage import LoginPage
from paginas.chamados import Chamados  # Certifique-se de importar a classe Chamados


def test_botao_novo_chamado(driver, login_info):
    LoginPage(driver).realizar_login(login_info)  # Realiza o login uma vez
    time.sleep(8)
    Chamados(driver).botao_criar_chamados()  # Chama a função botao_criar_chamados na página de Chamados
