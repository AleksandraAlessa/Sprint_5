from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarLocators
from data import MAIN_URL
import pytest

@pytest.mark.parametrize("tab_locator, expected_text", [
    (StellarLocators.SAUCES_TAB, "Соусы"),
    (StellarLocators.BUNS_TAB, "Булки"),
    (StellarLocators.FILLINGS_TAB, "Начинки")
])
def test_switch_tab(driver, tab_locator, expected_text):
    driver.get(MAIN_URL)
    driver.find_element(*tab_locator).click()
    active_text = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(*StellarLocators.ACTIVE_TAB).text
    )
    assert expected_text in active_text, f"Активная вкладка '{active_text}', ожидалась '{expected_text}'"
    