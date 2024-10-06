
#Открыть страницу https://SunInJuly.github.io/execute_script.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x.
#Проскроллить страницу вниз.
#Ввести ответ в текстовое поле.
#Выбрать checkbox "I'm the robot".
#Переключить radiobutton "Robots rule!".
#Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")


    x = browser.find_element(By.ID, "input_value").text
    
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "input.form-control")

    answer.send_keys(y)

    

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    
    
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
