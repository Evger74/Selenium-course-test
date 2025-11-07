from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"


browser = webdriver.Chrome()
try:
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    browser.find_element(By.NAME, "first_name").send_keys("Иван Иваныч")
    browser.find_element(By.NAME, "last_name").send_keys("Иванов")
    browser.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys("Челябинск")
    browser.find_element(By.ID, "country").send_keys("Россия")



finally:
    browser.quit()
