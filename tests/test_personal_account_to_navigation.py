from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_navigation_from_personal_account_to_constructor(driver, go_to_personal_account, log_out):
    # Переход в личный кабинет
    driver.find_element(By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']//p[text()='Личный Кабинет']").click()
    (WebDriverWait(driver, 5)
     .until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_button__14Yp3"))))

    # Переход к Конструктору
    driver.find_element(By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']//p[text()='Конструктор']").click()
    (WebDriverWait(driver, 10)
     .until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/")))


def test_navigation_from_personal_account_to_logo(driver, go_to_personal_account, log_out):
    # Переход в личный кабинет
    driver.find_element(By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']//p[text()='Личный Кабинет']").click()
    (WebDriverWait(driver, 5)
     .until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_button__14Yp3"))))

    # Переход на главную страницу
    driver.find_element(By.CLASS_NAME, 'AppHeader_header__logo__2D0X2').click()
    (WebDriverWait(driver, 10)
     .until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/")))

