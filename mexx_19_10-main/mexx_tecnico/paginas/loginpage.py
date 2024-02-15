import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def click_confirmar(self):
        # Clique no botão "Confirmar" padrão
        self.driver.find_element(By.CLASS_NAME, 'MuiButton-root').click()

        try:
            # Aguarde até 5 segundos para ver se o modal é exibido
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "css-bqvm4w"))
            )

            # Se o modal estiver visível, execute um script JavaScript para clicar no elemento com o seletor CSS
            script = """
                var element = document.querySelector('.css-bqvm4w');
                if (element) {
                    element.click();
                }
            """
            self.driver.execute_script(script)

            # Aguarde até que a nova página seja carregada
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be('https://demo.2do.mexx.ai/pt/calleds#/')
            )
        except TimeoutException:
            # Se o modal não for encontrado dentro do tempo limite, prossiga para a próxima página
            pass

    def realizar_login(self, login_info):
        email = login_info["email"]
        senha = login_info["senha"]


        email_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
        email_element.send_keys(email)


        senha_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        senha_element.send_keys(senha)


        self.click_confirmar()