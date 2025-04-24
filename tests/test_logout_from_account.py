
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import Locators
from curl import *

class TestLogout:
    """Тесты выхода из аккаунта"""

    def test_successful_logout(self, driver, login):

        # Используем WebDriver, который возвращает фикстура login
        driver = login

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACE_ORDER_BTN)
        ).text
        assert order_button == "Оформить заказ"

        driver.find_element(*Locators.ACCOUNT_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site + 'account/profile'))
        assert driver.current_url == main_site + 'account/profile'

        driver.find_element(*Locators.LOGOUT_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site + 'login'))
        assert driver.current_url == main_site + 'login'
        assert not driver.get_cookie("accessToken"), "Токен доступа не удален"


