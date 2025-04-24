
from selenium.webdriver.common.by import By

class Locators:
    # Локаторы для регистрации #и входа
    GO_TO_LOGIN_BTN = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]") # Кнопка "Войти в аккаунт"
    LOGIN_FORM_REG_LINK = (By.CLASS_NAME, "Auth_link__1fOlj") # Ссылка "Зарегистрироваться"
    FIELD_NAME = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")  # Поле "Имя"
    FIELD_EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input") # Поле "Email"
    FIELD_PASSWORD = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input") # Поле "Пароль"
    SIGN_IN_BTN = (By.XPATH, ".//button[contains(text(),'Войти')]") # Кнопка "Войти"
    REGISTER_BTN = (By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]") # Кнопка "Зарегистрироваться"
    REG_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Такой пользователь уже существует')]") # Ошибка Такой пользователь уже существует
    PASS_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]")

    # Локаторы для проверки входа
    PLACE_ORDER_BTN = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]") # Кнопка "Оформить заказ"
    ACCOUNT_BTN = (By.XPATH, "//a[@href='/account']") # Кнопка "Личный Кабинет"
    LOGIN_LINK_ON_REG_FORM = (By.XPATH, "//a[contains(@class, 'Auth_link') and contains(text(), 'Войти')]") # Ссылка "Войти" под формой регистрации
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]") # Ссылка "Восстановить пароль"
    LOGIN_LINK_ON_RECOVERY_FORM = (By.XPATH, "//a[contains(@class, 'Auth_link') and contains(text(), 'Войти')]") # Ссылка "Войти" на форме восстановления пароля

    PROFILE_SECTION = (By.XPATH, "//a[contains(@class, 'Account_link') and text()='Профиль']") # Ссылка на Профиль

    CONSTRUCTOR_BTN = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Кнопка "Конструктор"

    LOGO_SB = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__')]") # Логотип Stellar Burgers

    LOGOUT_BTN = (By.XPATH, "//button[contains(text(), 'Выход')]") # Кнопка выхода из аккаунта

    # Локаторы для раздела "Конструктор""
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div") # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div") # Раздел "Соусы"
    TOPPINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div") # Раздел "Начинки"
    ACTIVE_SECTION = (By.CSS_SELECTOR, "div.tab_tab_type_current__2BEPc") # Индикатор активного раздела
