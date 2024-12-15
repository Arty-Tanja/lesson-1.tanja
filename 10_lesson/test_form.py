from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.FormPage import InputFormPage
import allure

@allure.title("Автотест на заполнение формы")
@allure.description("Проверка цвета заполненных полей")
@allure.feature("Красный")
@allure.severity("critical")
def test_unput_form():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Открытие страницы с формой"):
        input_form = InputFormPage(browser)
    with allure.step("Заполнение поля имя"):
        input_form.first_name('Иван')
    with allure.step("Заполнение поля Фамилия"):
        input_form.last_name('Петров')
    with allure.step("Заполнение поля адрес"):
        input_form.address('Ленина, 55-3')
    with allure.step("Заполнение поля адрес почты"):
        input_form.e_mail('test@skypro.com')
    with allure.step("Заполнение поля номер телефона"):
        input_form.phone('+7985899998787')
    with allure.step("Оставляет пустым поле индекс"):
        input_form.zip_code('')
    with allure.step("Заполнение поля город"):
        input_form.city('Москва')
    with allure.step("Заполнение поля страна"):
        input_form.country('Россия')
    with allure.step("Заполнение поля профессия"):
        input_form.job_position('QA')
    with allure.step("Заполнение поля профессия"):
        input_form.company('SkyPro')
    with allure.step("Нажатие кнопки Отправить"):
        input_form.submit()

    with allure.step("Проверка подсвеченности цветом поля Zip code"):
        alert_danger = input_form.alert_danger()

        assert alert_danger == "rgba(248, 215, 218, 1)"

    with allure.step("Проверка подсвеченности зеленым заполненных полей"):
        alert_succes = input_form.alert_success()

        assert alert_succes == "rgba(209, 231, 221, 1)"

    with allure.step("Закрытие браузера"):
        browser.quit()