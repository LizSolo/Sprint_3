from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_personal_account_navigation(driver, go_to_personal_account, log_out):
    # Переход в личный кабинет
    driver.find_element(By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']//p[text()='Личный Кабинет']").click()

    # Проверка наличия элемента на странице личного кабинета
    (WebDriverWait(driver, 5)
     .until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_button__14Yp3"))))
