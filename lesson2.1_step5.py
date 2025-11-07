import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    #переходим по ссылке
    browser.get(link)
    #получаем число со страницы
    x_element = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    #конвертируем его в строку
    #x = x_element.text
    #вычисляем результат
    answer_x = calc(x_element)
    #ищем поле ответа
    answer_field = browser.find_element(By.ID, "answer")
    #вставляем ответ в поле
    answer_field.send_keys(answer_x)
    #отмечаем нужные кнопки
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(20)
    browser.quit()
