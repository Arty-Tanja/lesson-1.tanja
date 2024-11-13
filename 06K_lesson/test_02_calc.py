from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_screen():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    waiter = WebDriverWait(driver, 50)

    delay = driver.find_element(By.CSS_SELECTOR, '#delay')

    delay.clear()
    delay.send_keys('45')

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    screen_result = driver.find_element(By.CSS_SELECTOR, 'div.screen')
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )
    assert screen_result.text == "15"
    print(screen_result.text)

    driver.quit()

test_screen()