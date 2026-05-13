from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarLocators
from data import MAIN_URL


class TestLogout:
    def test_logout(self, driver, registered_user):
        # 1. Главная → нажать "Личный кабинет"
        driver.get(MAIN_URL)
        personal_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(StellarLocators.LOGIN_BUTTON_MAIN)
        )
        personal_btn.click()

        # 2. На странице входа заполнить email/пароль и нажать "Войти"
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL)
        )
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(registered_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(registered_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()

        # 3. После входа ждём главную страницу
        WebDriverWait(driver, 15).until(EC.url_to_be(MAIN_URL))

        # 4. Переходим в личный кабинет
        driver.find_element(*StellarLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(StellarLocators.LOGOUT_BUTTON)
        )

        # 5. Выход из аккаунта
        logout_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(StellarLocators.LOGOUT_BUTTON)
        )
        logout_btn.click()

        # 6. Проверяем URL
        assert MAIN_URL in driver.current_url