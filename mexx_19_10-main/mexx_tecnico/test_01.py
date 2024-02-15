import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from paginas.loginpage import LoginPage




def test_login(driver, login_info):
    LoginPage(driver).realizar_login(login_info)