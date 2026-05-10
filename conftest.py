import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from generators import generate_unique_email
from data import DEFAULT_PASSWORD, MAIN_URL
from locators import StellarLocators   # <-- обязательно импортировать!

@pytest.fixture(scope="session")
def registered_user():
    """Создаёт нового пользователя через UI и возвращает его данные.
    Фикстура выполняется один раз за сессию."""
    chrome_options = Options()
    chrome_options.add_argument('--no-proxy-server')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    email = generate_unique_email()
    password = DEFAULT_PASSWORD
    name = "Test_user"

    try:
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
        # Ждём появления полей регистрации
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(StellarLocators.REGISTER_NAME))
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(name)
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(password)
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        # Ждём, что регистрация прошла (редирект на страницу входа)
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(StellarLocators.LOGIN_SUBMIT))
    finally:
        driver.quit()

    return {"email": email, "password": password, "name": name}
# ------------------------------------------------------------
# Вспомогательная функция для входа (можно использовать в тестах)
# ------------------------------------------------------------
def login_user(driver, email, password):
    driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(email)
    driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(StellarLocators.CONSTRUCTOR_BUTTON)
    )

# ------------------------------------------------------------
# Основная фикстура драйвера для тестов (каждый тест – свой браузер)
# ------------------------------------------------------------
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-proxy-server')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

# ------------------------------------------------------------
# Фикстура для генерации уникального пользователя (если нужно прямо в тесте)
# ------------------------------------------------------------
@pytest.fixture
def new_user():
    email = generate_unique_email()
    password = DEFAULT_PASSWORD
    name = "Тестовый Пользователь"
    return {"email": email, "password": password, "name": name}