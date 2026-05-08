import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarLocators
from data import MAIN_URL

class TestLogin:

    # Вспомогательный метод для входа
    def _login(self, driver, email, password):
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(email)
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
    # Ждём, пока URL станет главной страницей
        WebDriverWait(driver, 5).until(EC.url_to_be(MAIN_URL))
    # Дополнительно ждём появления кнопки конструктора, чтобы убедиться в загрузке
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(StellarLocators.CONSTRUCTOR_BUTTON)
        )

    # 1. Вход по кнопке «Войти в аккаунт» на главной
    def test_login_main_button(self, driver, new_user):
        driver.get(MAIN_URL)
    # Переход на страницу входа
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
    # Теперь клик по ссылке "Зарегистрироваться"
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
    # Заполнение формы регистрации
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
    # После успешной регистрации возвращаемся на главную и входим
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
    # Ждём главную страницу
        WebDriverWait(driver, 5).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url

    # 2. Вход через кнопку «Личный кабинет»
    def test_login_via_personal_account(self, driver, new_user):
        driver.get(MAIN_URL)
    # Переход на страницу входа
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL))
    # Теперь клик по ссылке "Зарегистрироваться"
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
    # Заполнение формы регистрации
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
    # После успешной регистрации возвращаемся на главную и входим
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarLocators.LOGIN_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.LOGIN_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.LOGIN_SUBMIT).click()
    # Ждём главную страницу
        WebDriverWait(driver, 5).until(EC.url_to_be(MAIN_URL))
        assert "login" not in driver.current_url

    # 3. Вход через кнопку в форме регистрации
    def test_login_via_registration_form(self, driver, new_user):
        # Шаг 1: зарегистрировать нового пользователя
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL)
        )
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        # Регистрация завершена, пользователь создан

        # Шаг 2: перейти на страницу регистрации (там есть кнопка "Войти")
        driver.get(MAIN_URL + "register")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(StellarLocators.LOGIN_BUTTON_REGISTER_FORM)
        )
        # Кликнуть по кнопке "Войти" на странице регистрации
        driver.find_element(*StellarLocators.LOGIN_BUTTON_REGISTER_FORM).click()

        # Шаг 3: теперь мы на странице входа. Выполнить вход с данными new_user
        self._login(driver, new_user["email"], new_user["password"])

        # Шаг 4: проверка – URL должен быть главной страницей (без /login)
        assert "login" not in driver.current_url

    # Тест: вход через кнопку в форме восстановления пароля
    def test_login_via_recovery_form(self, driver, new_user):
        # Шаг 1: зарегистрировать нового пользователя (как выше)
        driver.get(MAIN_URL)
        driver.find_element(*StellarLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(StellarLocators.LOGIN_EMAIL)
        )
        driver.find_element(*StellarLocators.REGISTER_LINK).click()
        driver.find_element(*StellarLocators.REGISTER_NAME).send_keys(new_user["name"])
        driver.find_element(*StellarLocators.REGISTER_EMAIL).send_keys(new_user["email"])
        driver.find_element(*StellarLocators.REGISTER_PASSWORD).send_keys(new_user["password"])
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()

        # Шаг 2: перейти на страницу восстановления пароля
        driver.get(MAIN_URL + "forgot-password")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(StellarLocators.LOGIN_BUTTON_RECOVERY_FORM)
        )
        # Кликнуть по кнопке "Войти" на странице восстановления
        driver.find_element(*StellarLocators.LOGIN_BUTTON_RECOVERY_FORM).click()

        # Шаг 3: выполнить вход
        self._login(driver, new_user["email"], new_user["password"])

        # Шаг 4: проверка
        assert "login" not in driver.current_url