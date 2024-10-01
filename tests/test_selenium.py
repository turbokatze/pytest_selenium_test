import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonTest(unittest.TestCase):
    def setUp(self):
        service = Service()
        self.driver = webdriver.Chrome(service=service)

    def test_buy_item(self):
        self.driver.get('https://saucedemo.com')
        login_input = self.driver.find_element(By.ID, 'user-name')
        login_input.clear()
        login_input.send_keys('standard_user')
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys('secret_sauce')
        login_button = self.driver.find_element(By.ID, 'login-button')
        login_button.send_keys(Keys.ENTER)
        item_add = self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        item_add.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, 'shopping_cart_container').click()
        added = self.driver.find_element(By.CLASS_NAME, 'cart_item_label')
        if added.is_displayed():
            print('Item added')
        self.driver.find_element(By.ID, 'checkout').click()
        first_name_input = self.driver.find_element(By.ID, 'first-name')
        first_name_input.clear()
        first_name_input.send_keys('Ivan')
        last_name_input = self.driver.find_element(By.ID, 'last-name')
        last_name_input.clear()
        last_name_input.send_keys('Ivanov')
        last_name_input = self.driver.find_element(By.ID, 'postal-code')
        last_name_input.clear()
        last_name_input.send_keys('190000')
        self.driver.find_element(By.ID, 'continue').click()
        self.driver.find_element(By.ID, 'finish').click()
        completed = self.driver.find_element(By.CLASS_NAME, 'complete-text')
        if completed.is_displayed():
            assert True

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
