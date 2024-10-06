from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/alert_accept.html")


    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    browser.switch_to.alert.accept()

    x = browser.find_element(By.ID, "input_value").text

    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.TAG_NAME, "button").click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
