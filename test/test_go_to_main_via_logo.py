import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarLocators
from data import MAIN_URL

def test_go_to_main_via_logo(driver, new_user):
    driver.get(MAIN_URL)
    driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
    driver.find_element(*StellarLocators.REGISTER_LINK).click()
    driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
    driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
    driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
    driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
    driver.get(MAIN_URL)
    driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(new_user["email"])
    driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(new_user["password"])
    driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
    driver.find_element(*StellarLocators.PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGOUT_BUTTON))
    driver.find_element(*StellarLocators.LOGO).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.BUNS_TAB))
    assert driver.current_url == MAIN_URL