from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarLocators
from data import MAIN_URL

class TestLogout:
    def test_logout(self, driver, registered_user):
        # Вход с уже зарегистрированным пользователем
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(registered_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(registered_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        
        # Переход в личный кабинет
        driver.find_element(*StellarLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarLocators.LOGOUT_BUTTON))
        
        # Выход
        logout_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(StellarLocators.LOGOUT_BUTTON))
        logout_btn.click()
        
        # Проверка, что вернулись на главную
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(StellarLocators.LOGIN_BUTTON_MAIN))
        assert MAIN_URL in driver.current_url