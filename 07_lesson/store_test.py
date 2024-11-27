from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.StorePage import StorePage


def test_buy_on_store():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    buy = StorePage(browser)
    buy.username('standard_user')
    buy.password('secret_sauce')
    buy.add_to_cart()
    buy.shopping_cart()
    buy.checkout()
    buy.first_name('Tanya')
    buy.last_name('Mikurova')
    buy.postal_code('125599')
    buy.button_continue()
    total = buy.summary_total()

    assert total == 'Total: $58.29'

    browser.quit()