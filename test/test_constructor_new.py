from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarLocators
from data import MAIN_URL

def test_switch_to_buns(driver):
    driver.get(MAIN_URL)
    # Клик по "Соусы"
    driver.execute_script("arguments[0].click();", driver.find_element(*StellarLocators.SAUCES_TAB))
    WebDriverWait(driver, 5).until(lambda d: "Соусы" in d.find_element(*StellarLocators.ACTIVE_TAB).text)
    # Клик по "Булки"
    driver.execute_script("arguments[0].click();", driver.find_element(*StellarLocators.BUNS_TAB))
    WebDriverWait(driver, 5).until(lambda d: "Булки" in d.find_element(*StellarLocators.ACTIVE_TAB).text)
    # Клик по "Начинки"
    driver.execute_script("arguments[0].click();", driver.find_element(*StellarLocators.FILLINGS_TAB))
    WebDriverWait(driver, 5).until(lambda d: "Начинки" in d.find_element(*StellarLocators.ACTIVE_TAB).text)
    active = driver.find_element(*StellarLocators.ACTIVE_TAB).text
    assert "Начинки" in active