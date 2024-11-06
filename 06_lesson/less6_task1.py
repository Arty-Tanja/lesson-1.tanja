from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(20)

driver.find_element(By.CSS_SELECTOR, "button#ajaxButton").click()
phrase = driver.find_element(By.CSS_SELECTOR, "p.bg-success")

print(phrase.text)

driver.quit()