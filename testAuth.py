import time
import os

from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

s = Service()
driver = webdriver.Safari(service=s)

try:
    driver.maximize_window()
    driver.get('https://saucedemo.com')
    time.sleep(1)

    login_input = driver.find_element(By.ID, 'user-name')
    login_input.clear()
    login_input.send_keys('standard_user')
    time.sleep(1)

    password_input = driver.find_element(By.ID, 'password')
    password_input.clear()
    password_input.send_keys('secret_sauce')
    time.sleep(1)

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.send_keys(Keys.ENTER)
    time.sleep(1)

    itemToBuy = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    itemToBuy.send_keys(Keys.ENTER)
    time.sleep(1)

    checkCart = driver.find_element(By.ID, 'shopping_cart_container').click()
    time.sleep(1)

    proceedCheckout = driver.find_element(By.ID, 'checkout').click()
    time.sleep(1)

    firstNameInput = driver.find_element(By.ID, 'first-name')
    firstNameInput.clear()
    firstNameInput.send_keys('FirstName')
    time.sleep(1)

    lastNameInput = driver.find_element(By.ID, 'last-name')
    lastNameInput.clear()
    lastNameInput.send_keys('LastName')
    time.sleep(1)

    lastNameInput = driver.find_element(By.ID, 'postal-code')
    lastNameInput.clear()
    lastNameInput.send_keys('190000')
    time.sleep(1)

    confirmCheckout = driver.find_element(By.ID, 'continue').click()
    time.sleep(1)

    finishOrder = driver.find_element(By.ID, 'finish').click()
    time.sleep(1)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
