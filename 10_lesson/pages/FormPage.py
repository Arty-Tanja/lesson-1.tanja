from selenium.webdriver.common.by import By
import allure


class InputFormPage():
    """
    Класс содержит методы для заполнения, отправки формы, и проверки цвета фона поля
    """
    def __init__(self, driver: str):
        """
        Открывет страницу с формой для золнения
        """
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    def first_name(self, term: str):
        """
        Заполняет значением поле имя
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(term)

    def last_name(self, term: str):
        """
        Заполняет значением поле фамилия
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(term)

    def address(self, term: str):
        """
        Заполняет значением поле адрес
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(term)

    def zip_code(self, term: str):
        """
        Заполняет значением поле индекс
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys(term)

    def city(self, term: str):
        """
        Заполняет значением поле город
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(term)

    def country(self, term: str):
        """
        Заполняет значением поле страна
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(term)

    def e_mail(self, term: str):
        """
        Заполняет значением поле e-mail
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(term)

    def phone(self, term: str):
        """
        Заполняет значением поле номер телефона
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(term)

    def job_position(self, term: str):
        """
        Заполняет значением поле профессия
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(term)

    def company(self, term: str):
        """
        Заполняет значением поле компания
        """
        self._driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(term)

    def submit(self):
        """
        Нажимает на кнопку Отправить
        """
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def alert_danger(self) -> str:
        """
        Проверяет подсвеченность поля zip-code красным
        """
        alert_danger = self._driver.find_element(By.CSS_SELECTOR, 'div.alert.py-2.alert-danger').value_of_css_property("background-color")
        return alert_danger

    def alert_success(self) -> list:
        """
        Выводит список полей, заполненных зеленым
        """
        alert_success = self._driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2.alert-success')
        for form in alert_success:
            return form.value_of_css_property("background-color")