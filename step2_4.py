from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from calc import calc
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element()
        # EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
button = browser.find_element(By.TAG_NAME, 'button')
button.click()

elem = browser.find_element(By.ID, "input_value").text
y = calc(elem)

_input = browser.find_element(By.ID, "answer")
_input.send_keys(y)

button = browser.find_element(By.ID, 'solve')
button.click()

print(browser.switch_to.alert.text)

time.sleep(20)

# print(browser.switch_to.alert.text)
# message = browser.find_element(By.ID, "book")
# message.click()

# assert "successful" in message.text