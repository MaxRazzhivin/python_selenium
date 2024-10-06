from selenium import webdriver
from selenium.webdriver.common.by import By

import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")

    answer1 = browser.find_element(By.CSS_SELECTOR, "[name=firstname]").send_keys("123")
    answer2 = browser.find_element(By.CSS_SELECTOR, "[name=lastname]").send_keys("123")
    answer3 = browser.find_element(By.CSS_SELECTOR, "[name=email]").send_keys("123")

    browser.find_element(By.ID, "file").send_keys("/Users/maxnovo/Desktop/Python/selenium_course/test.txt")

    

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
