
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import Locators
from curl import *

class TestAccountToConstructorNavigation:

    def test_navigate_via_constructor_button(self, driver):
        driver.find_element(*Locators.GO_TO_LOGIN_BTN).click()

        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)

        driver.find_element(*Locators.SIGN_IN_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        driver.find_element(*Locators.ACCOUNT_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site + 'account/profile'))
        assert driver.current_url == main_site + 'account/profile'

        driver.find_element(*Locators.CONSTRUCTOR_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    def test_navigate_via_logo(self, driver):
        driver.find_element(*Locators.GO_TO_LOGIN_BTN).click()

        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)

        driver.find_element(*Locators.SIGN_IN_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        driver.find_element(*Locators.ACCOUNT_BTN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site + 'account/profile'))
        assert driver.current_url == main_site + 'account/profile'

        driver.find_element(*Locators.LOGO_SB).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site
