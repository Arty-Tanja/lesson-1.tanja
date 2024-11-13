from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

try:
    waiting = WebDriverWait(driver, 10)

    waiting.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()

    waiting.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    waiting.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        )
    ).click()

    waiting.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))
    ).click()

    waiting.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    ).click()

    waiting.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    waiting.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Tanja")

    waiting.until(
        EC.presence_of_element_located((By.ID, "last-name"))
    ).send_keys("Mikurova")

    waiting.until(
        EC.presence_of_element_located((By.ID, "postal-code"))
    ).send_keys("125599")

    waiting.until(
        EC.element_to_be_clickable((By.ID, "continue"))
    ).click()

    total_price_element = waiting.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_price = total_price_element.text

    assert total_price == "Total: $58.29"

    print(total_price)

finally:
    driver.quit()