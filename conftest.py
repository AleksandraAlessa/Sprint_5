import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from generators import generate_unique_email
from data import DEFAULT_PASSWORD

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-proxy-server')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def new_user():
    email = generate_unique_email()
    password = DEFAULT_PASSWORD
    name = "Тестовый Пользователь"
    return {"email": email, "password": password, "name": name}