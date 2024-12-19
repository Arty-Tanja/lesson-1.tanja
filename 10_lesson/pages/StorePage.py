from selenium.webdriver.common.by import By
import allure


class StorePage():
    """
    Класс содержит методы по авторизации на сайте, добавлению товаров в корзину и выводу итоговой суммы
    """
    def __init__(self, driver: str):
        """
        Открывает сайт магазина
        """
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')

    def username(self, term: str):
        """
        Заполняет поле логин
        """
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(term)

    def password(self, term: str):
        """
        Заполняет поле пароль и нажимает на кнопку войти
        """
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_to_cart(self):
        """
        Находит нужные товары и нажимает кнопку В корзину
        """
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def shopping_cart(self):
        """
        Переходит на страницу с корзиной
        """
        self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    def checkout(self):
        """
        Нажимает на кнопку checkout
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def first_name(self, term: str):
        """
        Запоняет поле имя формы заказа
        """
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(term)

    def last_name(self, term: str):
        """
        Заполняет поле фамилия формы заказа
        """
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(term)

    def postal_code(self, term: str):
        """
        Заполняет поле индекс
        """
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(term)

    def button_continue(self):
        """
        Нажимает на кнопку продолжить
        """
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def summary_total(self) -> str:
        """
        Выводит итоговую сумму в виде текста
        """
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return total 