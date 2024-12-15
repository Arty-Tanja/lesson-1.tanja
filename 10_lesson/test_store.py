from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.StorePage import StorePage
import allure

@allure.title("Автотест на оформление заказа в интернет-магазине")
@allure.description("Авторизация, добавление товаров в корзину, оформление заказа")
@allure.feature("Интернет-магазин")
@allure.severity("critical")
def test_buy_on_store():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Открытие сайта магазина: https://www.saucedemo.com/"):
        buy = StorePage(browser)
    with allure.step("Ввод standard_user в поле Username"):
        buy.username('standard_user')
    with allure.step("Ввод secret_sauce в поле Password"):
        buy.password('secret_sauce')
    with allure.step("Добавление в корзину товаров"):
        buy.add_to_cart()
    with allure.step("Переход в корзину"):
        buy.shopping_cart()
    with allure.step("Нажатие Checkout"):
        buy.checkout()
    with allure.step("Заполнение поля First Name"):
        buy.first_name('Tanya')
    with allure.step("Заполнение поля Last Name"):
        buy.last_name('Mikurova')
    with allure.step("Заполнение поля Zip/Postal Code"):
        buy.postal_code('125599')
    with allure.step("Нажатие кнопки Продолжить"):
        buy.button_continue()
    with allure.step("Вывод Итоговой стоимости (Total)"):
        total = buy.summary_total()

    with allure.step("Проверка Итоговой стоимости (Total)"):
        assert total == 'Total: $58.29'

    with allure.step("Закрытие браузера"):
        browser.quit()