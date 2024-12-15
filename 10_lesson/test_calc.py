from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalculatorPage
import allure

@allure.title("Автотест на операции калькулятора")
@allure.description("Проверка результата операции через установленное время")
@allure.feature("Калькулятор")
@allure.severity("critical")
def test_calculator():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Открытие сайта с калькулятором"):
        calculator = CalculatorPage(browser)
    with allure.step("Установка задержки 45 секунд"):
        calculator.delay('45')

    with allure.step("Нажатие 7+8="):
        calculator.click()

    with allure.step("Ожидание роявления результата"):
        screen = calculator.screen()

    with allure.step("Проверка ответа"):
        assert screen == '15'

    with allure.step("Закрытие браузера"):
        browser.quit()