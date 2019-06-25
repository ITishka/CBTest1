from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import os
import glob


@Given('пользователь на странице "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.get(url)


@Then('отображается поле "{text}"')
def step(context, text):
    try:
        assert context.browser.find_element_by_xpath('//*[@title="' + text + '"]')
    except Exception:
        print("Поле " + text + " не появилось")


@Then('ввели в поле "{text1}" "{text2}"')
def step(context, text1, text2):
    elem = context.browser.find_element_by_name(text1)
    elem.send_keys(text2)
    elem.send_keys(Keys.RETURN)


@Then('дождались загрузки страницы "{text}"')
def step(context, text):
    try:
        WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.ID, text)))
    except Exception:
        print("Страница не загрузилась")


@When('нажали на ссылку "{text}"')
def step(context, text):
    elem = context.browser.find_element_by_partial_link_text(text)
    href = elem.get_attribute('href')
    context.browser.get(href)


@Then('вышло сообщение "{text}"')
def step(context, text):
    try:
        WebDriverWait(context.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[text()="' + text + '"]')))
    except Exception:
        print("Сообщение не появилось")


@When('сняли чек-бокс "{text}"')
def step(context, text):
    context.browser.find_element_by_xpath("//*[contains(text(), '" + text + "')]").click()


@When('сделали скриншот')
def step(context):
    name = str(datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
    context.browser.save_screenshot('./screen/screen' + name + '.png')


@Then('выбрали из списка "{text}"')
def step(context, text):
    context.browser.find_element_by_xpath("//select/option[@value='" + text + "']").click()


@When('запомнили текст1 "{text}"')
def step(context, text):
    tx1 = context.browser.find_element_by_class_name(text).text
    f = open("genius_idea.txt", "w+")
    f.write(tx1 + '\n')
    f.close()


@When('запомнили текст2 "{text}"')
def step(context, text):
    tx2 = context.browser.find_element_by_class_name(text).text
    f = open("genius_idea.txt", "a+")
    f.write(tx2 + '\n')
    f.close()


@Then('сравнили текст1 и текст2')
def step(context):
    f = open("genius_idea.txt", "r+")
    tx1 = f.readline()
    tx2 = f.readline()
    if tx1 != tx2:
        print(tx1 + " не равно " + tx2)
    else:
        print(tx1 + " равно " + tx2)
    f.close()


@When('удалили скрины')
def step(context):
    files = glob.glob('./screen/*.png')
    for f in files:
        os.remove(f)

@When('закончили тест')
def step(context):
    context.browser.quit()
