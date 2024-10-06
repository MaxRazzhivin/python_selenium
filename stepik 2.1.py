from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    xb = browser.find_element(By.ID, "input_value")
    x = xb.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
