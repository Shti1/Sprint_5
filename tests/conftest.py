import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    """
    Фикстура для авторизации пользователя.
    """
    # Вводим email в поле "Email", пароль в поле "Пароль"
    driver.find_element(*Locators.GO_TO_LOGIN_BTN).click()
    driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.SIGN_IN_BTN).click()

    return driver