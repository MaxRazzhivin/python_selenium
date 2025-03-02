from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    value = browser.find_element(By.ID, 'price')

    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    x = browser.find_element(By.ID, "input_value").text

    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "solve").click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
