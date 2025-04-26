from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from locators import Locators
from curl import *

class TestPersonalAccountNavigation:
    """Тесты перехода в личный кабинет"""

    def test_personal_account_navigation(self, driver):

        # 1. Клик по кнопке "Личный кабинет" (без авторизации)
        driver.find_element(*Locators.ACCOUNT_BTN).click()

        # 2. Проверка редиректа на страницу авторизации
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site + 'login'))
        # assert
        assert driver.current_url == main_site + 'login'

        # 3. Авторизация
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)

        driver.find_element(*Locators.SIGN_IN_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACE_ORDER_BTN)
        ).text
        assert order_button == Messages.order_button

        # 4. Повторный переход в личный кабинет после авторизации
        driver.find_element(*Locators.ACCOUNT_BTN).click()

        # 5. Проверка успешного перехода
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site + 'account/profile'))
        # assert
        assert driver.current_url == main_site + 'account/profile'