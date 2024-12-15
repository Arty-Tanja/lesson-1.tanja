from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure


class CalculatorPage():
    """
    Содержит методы для работы с калькулятором
    """
    def __init__(self, driver: str):
        """
        Открывает страницу с калькулятором и устанавливает ожидание
        """
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(50)

    def delay(self, term: int):
        """
        Установка времени задержки секунд
        """
        delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(term)

    def click(self):
        """
        Находит кнопки калькулятора и нажимает их
        """
        self._driver.find_element(By.XPATH, "//*[contains(text(),'7')]").click()
        self._driver.find_element(By.XPATH, "//*[contains(text(),'+')]").click()
        self._driver.find_element(By.XPATH, "//*[contains(text(),'8')]").click()
        self._driver.find_element(By.XPATH, "//*[contains(text(),'=')]").click()

    def screen(self) -> str:
        """
        Ожидает результат вычислений и возвращает текст на экране калькулятора
        """
        screen = self._driver.find_element(By.CSS_SELECTOR, 'div.screen')
        WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
        )
        return screen.text