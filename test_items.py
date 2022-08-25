from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket(browser):
        browser.get(link)
        time.sleep(30)
        add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
        assert add_to_basket, 'Add to basket button is not found!'
        