from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pytest

class Atribuir_tec:
    def __init__(self,driver):
        self.driver = driver

    def abrir_chamado(self):
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/main/main/div/div[6]/div/div[1]').click()
        time.sleep(10)
