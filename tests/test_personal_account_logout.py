from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_personal_account_logout(driver, go_to_personal_account):
    # Переход в личный кабинет
    driver.find_element(By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']//p[text()='Личный Кабинет']").click()
    (WebDriverWait(driver, 5)
     .until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_button__14Yp3"))))

    # Выход из аккаунта
    driver.find_element(By.CLASS_NAME, "Account_button__14Yp3").click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
