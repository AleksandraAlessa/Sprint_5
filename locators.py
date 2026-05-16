from selenium.webdriver.common.by import By

class StellarLocators:
    # ---------- Регистрация ----------
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
# Поле Имя: первое текстовое поле на форме
    REGISTER_NAME = (By.XPATH, "(//input[@type='text'])[1]")
# Поле Email: второе текстовое поле на форме
    REGISTER_EMAIL = (By.XPATH, "(//input[@type='text'])[2]")
# Поле Пароль: поле с type='password'
    REGISTER_PASSWORD = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTER_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")

    # ---------- Вход ----------
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # главная страница
    LOGIN_BUTTON_PERSONAL = (By.XPATH, "//a[text()='Личный кабинет']") # кнопка в хедере (если не авторизован)
    LOGIN_BUTTON_REGISTER_FORM = (By.XPATH, "//a[text()='Войти']")  # на странице регистрации
    LOGIN_BUTTON_RECOVERY_FORM = (By.XPATH, "//a[text()='Войти']")  # на странице восстановления пароля
    LOGIN_EMAIL = (By.NAME, "name")  # поле "Email" на форме входа
    LOGIN_PASSWORD = (By.NAME, "Пароль")  # поле "Пароль" на форме входа
    LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"

    # ---------- Личный кабинет ----------
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")  # ссылка в хедере (авторизован)
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # в личном кабинете

    # ---------- Конструктор и логотип ----------
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка в хедере
    LOGO = (By.XPATH, "//a[contains(@href, '/')]//*[local-name()='svg']")  # логотип Stellar Burgers

    # ---------- Вкладки конструктора ----------
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span")