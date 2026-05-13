import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarLocators
from data import MAIN_URL

class TestLogin:

    def test_login_main_button(self, driver, registered_user):
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(registered_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(registered_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url

    def test_login_via_personal_account(self, driver, registered_user):
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(registered_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(registered_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url

    def test_login_via_registration_form(self, driver, registered_user):
        driver.get(MAIN_URL + "register")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_BUTTON_REGISTER_FORM))
        driver.find_element(*StellarLocators.LOGIN_BUTTON_REGISTER_FORM).click()
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(registered_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(registered_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url

    def test_login_via_recovery_form(self, driver, registered_user):
        driver.get(MAIN_URL + "forgot-password")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_BUTTON_RECOVERY_FORM))
        driver.find_element(*StellarLocators.LOGIN_BUTTON_RECOVERY_FORM).click()
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(registered_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(registered_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url
        