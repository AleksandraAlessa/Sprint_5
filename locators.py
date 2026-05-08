from selenium.webdriver.common.by import By

class StellarLocators:
    # ---------- Регистрация ----------
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # ссылка на страницу регистрации
    REGISTER_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # поле "Имя"
    REGISTER_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # поле "Email"
    REGISTER_PASSWORD = (By.NAME, "Пароль")  # поле "Пароль" (атрибут name)
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTER_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # ошибка под полем

    # ---------- Вход ----------
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # главная страница
    LOGIN_BUTTON_PERSONAL = (By.XPATH, "//a[text()='Личный кабинет']")  # кнопка в хедере (если не авторизован)
    LOGIN_BUTTON_REGISTER_FORM = (By.XPATH, "//a[text()='Войти']")  # на странице регистрации
    LOGIN_BUTTON_RECOVERY_FORM = (By.XPATH, "//a[text()='Войти']")  # на странице восстановления пароля
    LOGIN_EMAIL = (By.XPATH, "//input[@name='name']")  # поле "Email" на форме входа
    LOGIN_PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # поле "Пароль" на форме входа
    LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"

    # ---------- Личный кабинет ----------
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")  # ссылка в хедере (авторизован)
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # в личном кабинете

    # ---------- Конструктор и логотип ----------
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка в хедере
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")  # логотип Stellar Burgers

    # ---------- Вкладки конструктора ----------
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span")