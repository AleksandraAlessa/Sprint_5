import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarLocators
from data import MAIN_URL

class TestLogin:

    def test_login_main_button(self, driver, new_user):
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
        # регистрация
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        # возврат на главную и вход
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url

    def test_login_via_personal_account(self, driver, new_user):
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_PERSONAL).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_PERSONAL).click()
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url

    def test_login_via_registration_form(self, driver, new_user):
        driver.get(MAIN_URL + "register")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_BUTTON_REGISTER_FORM))
        driver.find_element(*StellarLocators.LOGIN_BUTTON_REGISTER_FORM).click()
        driver.find_element(*StellarLocators.REGISTER_LINK).click()  # всё равно нужно зарегистрироваться
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        driver.get(MAIN_URL + "login")  # теперь вход
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url

    def test_login_via_recovery_form(self, driver, new_user):
        driver.get(MAIN_URL + "forgot-password")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_BUTTON_RECOVERY_FORM))
        driver.find_element(*StellarLocators.LOGIN_BUTTON_RECOVERY_FORM).click()
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        driver.get(MAIN_URL + "login")
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url