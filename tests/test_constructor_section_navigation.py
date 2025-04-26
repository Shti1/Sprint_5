
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestConstructorSectionNavigation:

    def test_switch_to_sauces_section(self, driver):

        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION)
        )
        sauces_tab.click()

        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert active_tab.text == "Соусы"
        assert "current" in sauces_tab.get_attribute("class")

    def test_switch_to_toppings_section(self, driver):

        toppings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.TOPPINGS_SECTION)
        )
        toppings_tab.click()

        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert active_tab.text == "Начинки"
        assert "current" in toppings_tab.get_attribute("class")

    def test_switch_to_buns_section(self, driver):

        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION)
        )
        sauces_tab.click()

        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUNS_SECTION)
        )

        buns_tab.click()

        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert active_tab.text == "Булки"
        assert "current" in buns_tab.get_attribute("class")