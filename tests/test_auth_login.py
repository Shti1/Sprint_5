
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from locators import Locators
from curl import *

class TestLogin:
    """Тесты для проверки входа в систему."""

    def test_login_via_main_button(self, driver, login):
        """Проверка входа через кнопку 'Войти в аккаунт' на главной."""

        # Используем WebDriver, который возвращает фикстура login
        driver = login

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACE_ORDER_BTN)
        ).text
        assert order_button == Messages.order_button

    def test_login_via_personal_account_button(self, driver):
        """Проверка входа через кнопку 'Личный кабинет'."""
        # Нажимаем кнопку "Личный кабинет"
        driver.find_element(*Locators.ACCOUNT_BTN).click()

        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)

        driver.find_element(*Locators.SIGN_IN_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACE_ORDER_BTN)
        ).text
        assert order_button == Messages.order_button

    def test_login_via_registration_form(self, driver):
        """Проверка входа через кнопку в форме регистрации."""
        # Переходим на форму регистрации
        driver.find_element(*Locators.GO_TO_LOGIN_BTN).click()
        driver.find_element(*Locators.LOGIN_FORM_REG_LINK).click()

        # Нажимаем "Войти" на форме регистрации
        driver.find_element(*Locators.LOGIN_LINK_ON_REG_FORM).click()

        # Заполняем и отправляем форму входа
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)

        # Проверяем успешный вход
        driver.find_element(*Locators.SIGN_IN_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACE_ORDER_BTN)
        ).text
        assert order_button == Messages.order_button

    def test_login_via_password_recovery_form(self, driver):
        """Проверка входа через кнопку в форме восстановления пароля."""
        # Переходим на форму входа
        driver.find_element(*Locators.GO_TO_LOGIN_BTN).click()

        # Переходим на форму восстановления пароля
        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()

        # Нажимаем "Войти" на форме восстановления пароля
        driver.find_element(*Locators.LOGIN_LINK_ON_RECOVERY_FORM).click()

        # Заполняем и отправляем форму входа
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)

        # Проверяем успешный вход
        driver.find_element(*Locators.SIGN_IN_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PLACE_ORDER_BTN)
        ).text
        assert order_button == Messages.order_button
