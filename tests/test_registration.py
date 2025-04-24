
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        #arrange
        name, email, password = generate_registration_data()

        driver.find_element(*Locators.GO_TO_LOGIN_BTN).click()
        driver.find_element(*Locators.LOGIN_FORM_REG_LINK).click()

        driver.find_element(*Locators.FIELD_NAME).send_keys(name)
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)

        assert name.strip() != "", "Поле 'Имя' не должно быть пустым"
        assert "@" in email and "." in email.split("@")[1], "Неверный формат email"
        assert len(password) >= 6, "Пароль должен содержать минимум 6 символов"

        #act
        driver.find_element(*Locators.REGISTER_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site + 'login'))
        #assert
        assert driver.current_url == main_site + 'login'

    def test_password_validation(self, driver):

        # Переход на форму регистрации
        driver.find_element(*Locators.GO_TO_LOGIN_BTN).click()
        driver.find_element(*Locators.LOGIN_FORM_REG_LINK).click()

        # Заполнение формы (пароль менее 6)
        name, email, _ = generate_registration_data()
        driver.find_element(*Locators.FIELD_NAME).send_keys(name)
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys("12345")

        # Отправка формы
        driver.find_element(*Locators.REGISTER_BTN).click()

        # Проверка ошибки
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PASS_ERROR)
        ).text

        assert error_message == 'Некорректный пароль'

class TestCheckingCreationExistingAccount:

    def test_failed_registration(self, driver):
        driver.find_element(*Locators.GO_TO_LOGIN_BTN).click()
        driver.find_element(*Locators.LOGIN_FORM_REG_LINK).click()
        driver.find_element(*Locators.FIELD_NAME).send_keys(Credentials.name)
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BTN).click()

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REG_ERROR)
        ).text

        assert error_message == 'Такой пользователь уже существует'