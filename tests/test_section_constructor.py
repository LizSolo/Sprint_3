import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from config import Config
from locators import Locators


@pytest.mark.parametrize("tab_name, tab_xpath, header_xpath", [
    ("Начинки", './/span[text()="Начинки"]', './/h2[text()="Начинки"]'),
    ("Соусы", './/span[text()="Соусы"]', './/h2[text()="Соусы"]'),
    ("Булки", './/span[text()="Булки"]', './/h2[text()="Булки"]'),
])
def test_navigation_tabs(driver, tab_name, tab_xpath, header_xpath):
    driver.get(Config.BASE_URL)
    # Переход на страницу конструктора
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    # Если вкладка Булки активна, переключаемся на другую вкладку
    if tab_name == "Булки":
        # Если вкладка Булки уже активна, сначала переключаемся на другую вкладку (например, Соусы)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH,
                                              './/div[contains(@class, "tab_tab__1SPyG tab_tab_type_current__2BEPc") and contains(.,"Булки")]'))
        )
        # Переключаемся на вкладку Соусы
        driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH,
                                              './/div[contains(@class, "tab_tab__1SPyG tab_tab_type_current__2BEPc") and contains(.,"Соусы")]'))
        )

    # Клик на вкладку
    driver.find_element(By.XPATH, tab_xpath).click()

    # Ожидание активного состояния вкладки
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH,
                                          f'.//div[contains(@class, "tab_tab__1SPyG tab_tab_type_current__2BEPc") and contains(.,"{tab_name}")]'))
    )

    # Проверка заголовка вкладки
    header_element = driver.find_element(By.XPATH, header_xpath)
    assert header_element.text == tab_name
