import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from generators import generate_unique_email
from data import DEFAULT_PASSWORD, MAIN_URL
from locators import StellarLocators
from test_data import TEST_USER   # импортируем статические данные

# ------------------------------------------------------------
# Вспомогательная функция для входа (необязательно)
# ------------------------------------------------------------
def login_user(driver, email, password):
    driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(email)
    driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.CONSTRUCTOR_BUTTON))

# ------------------------------------------------------------
# Фикстура с заранее зарегистрированным пользователем (для тестов входа и т.д.)
# ------------------------------------------------------------
@pytest.fixture(scope="session")
def registered_user():
    return TEST_USER

# ------------------------------------------------------------
# Основная фикстура драйвера
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
# Фикстура для тестов регистрации (генерирует нового пользователя)
# ------------------------------------------------------------
@pytest.fixture
def new_user():
    email = generate_unique_email()
    password = DEFAULT_PASSWORD
    name = "Тестовый Пользователь"
    return {"email": email, "password": password, "name": name}
