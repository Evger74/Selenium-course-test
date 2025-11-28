import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
# result = 0
url = 'https://parsinger.ru/selenium/5.5/5/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    # ждём загрузки полей
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'main-container'))
    )
    #собираем список полей со страницы
    fields = browser.find_elements(By.CSS_SELECTOR, '#main-container > [style]')
    for field in fields:
        #получаем цвет контейнера
        color = field.find_element(By.TAG_NAME, 'span').text
        #выбираем выпадающий список
        drop_list = Select(field.find_element(By.TAG_NAME, 'select'))
        #устанавливаем нужный цвет в списке
        drop_list.select_by_visible_text(color)
        #нажимаем кнопку нужного цвета
        field.find_element(By.CSS_SELECTOR, f'[data-hex="{color}"]').click()
        #ставим галочку в чекбоксе
        field.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
        #вставляем цвет в текстовое поле
        field.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys(color)
        #жмём кнопку Проверить
        field.find_element(By.XPATH, '//button[contains(text(), "Проверить")]').click()

    browser.find_element(By.CSS_SELECTOR, 'body > button:last-child').click()
    print(browser.switch_to.alert.text)

    time.sleep(10)