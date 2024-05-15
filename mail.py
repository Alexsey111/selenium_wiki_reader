from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import keyboard

def selections():
    while True:
        print('Выберите вариант действия (1, 2 или 3):')
        print('1 - листать параграфы статьи (с помощью клавиши Enter);')
        print('2 - перейти на одну из связанных страниц;')
        print('3 - выход (нажмите "Esc").')

        key = keyboard.read_key()
        if key == '1':
            return 1
        elif key == '2':
            return 2
        elif key == '3' or key == 'Esc':
            return 3

def transition(num):
    if num == 1:
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        for paragraph in paragraphs:
            print(paragraph.text)
            input("Нажмите Enter для перехода к следующему параграфу...")
    else:
        links = browser.find_elements(By.TAG_NAME, 'a')
        if links:
            valid_links = [link.get_attribute('href') for link in links if link.get_attribute('href') and '/wiki/' in link.get_attribute('href')]
            if valid_links:
                link = random.choice(valid_links)
                print(f"Переход по ссылке: {link}")
                browser.get(link)
            else:
                print("Не найдены валидные ссылки для перехода.")
        else:
            print("Не найдены ссылки на странице.")

if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

    assert 'Википедия' in browser.title
    time.sleep(5)

    search_box = browser.find_element(By.ID, 'searchInput')
    enquiry = input('Введите поисковый запрос: ')
    search_box.send_keys(enquiry)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    elements = browser.find_elements(By.PARTIAL_LINK_TEXT, enquiry)
    if elements:
        element = random.choice(elements)
        element.click()
    else:
        print(f"Элемент с частичным текстом '{enquiry}' не найден.")
        browser.quit()
        exit()

    while True:
        num = selections()
        if num == 3:
            print("Выход из программы.")
            break
        transition(num)

    browser.quit()