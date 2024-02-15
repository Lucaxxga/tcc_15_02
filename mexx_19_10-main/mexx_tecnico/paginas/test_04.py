import pytest
import time
from mexx_tecnico.paginas.loginpage import LoginPage
from mexx_tecnico.test_01 import realizar_login
from mexx_tecnico.paginas.atribuir_tec import Atribuir_tec  # Certifique-se de importar a classe Chamados


def finalizar_chamado_tec_adm(driver, login_info):
    realizar_login(driver, login_info)  # Realiza o login uma vez
    abrir
