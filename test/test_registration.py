import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarLocators
from data import MAIN_URL, INCORRECT_PASSWORD

class TestRegistration:

    def test_successful_registration(self, driver, new_user):
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_SUBMIT))
        assert driver.current_url == MAIN_URL + "login"

    def test_registration_invalid_password_error(self, driver, new_user):
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(INCORRECT_PASSWORD)
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        error = driver.find_element(*StellarLocators.REGISTER_ERROR)
        assert error.text == "Некорректный пароль"
        