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


# удаление старых скринов и создание/очистка файла genius_idea.txt
@Then('очистили среду')
def step(context):
    files = glob.glob('./screen/*.png')
    for s in files:
        os.remove(s)

    with open('genius_idea.txt', 'w+', encoding='utf-8') as f:
        f.write('')


@Then('отображается поле "{pole}"')
def step(context, pole):
    try:
        assert context.browser.find_element_by_xpath('//*[@title="{}"]'.format(pole))
    except Exception:
        print("Поле {} не появилось".format(pole))


@Then('ввели в поле "{pole}" "{text}"')
def step(context, pole, text):
    d = dict(Поиск='//*[@title="Поиск"]',
             email='//*[@name="email"]')
    elem = context.browser.find_element_by_xpath(d[pole])
    elem.send_keys(text)
    elem.send_keys(Keys.RETURN)


@Then('дождались загрузки страницы "{page}"')
def step(context, page):
    try:
        WebDriverWait(context.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "{}")]'.format(page))))
    except Exception:
        print("Страница не загрузилась")


@When('нажали на ссылку "{textlink}"')
def step(context, textlink):
    elem = context.browser.find_element_by_partial_link_text(textlink)
    href = elem.get_attribute('href')
    context.browser.get(href)


@Then('вышло сообщение "{text}"')
def step(context, text):
    try:
        WebDriverWait(context.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[text()="{}"]'.format(text))))
    except Exception:
        print("Сообщение не появилось")


@When('сняли чек-бокс "{flag}"')
def step(context, flag):
    context.browser.find_element_by_xpath("//*[contains(text(), '{}')]".format(flag)).click()


@When('сделали скриншот')
def step(context):
    name = str(datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
    context.browser.save_screenshot('./screen/screen{}.png'.format(name))


@Then('выбрали из списка "{text}"')
def step(context, text):
    context.browser.find_element_by_xpath("//select/option[@value='{}']".format(text)).click()


@When('запомнили текст из {text}')
def step(context, text):
    d = dict(заголовка='shadow-box__title')
    tx = context.browser.find_element_by_class_name(d[text]).text
    with open('genius_idea.txt', 'a') as f:
        f.write(tx + '\n')


@Then('сравнили запомненные тексты')
def step(context):
    with open('genius_idea.txt', 'r+') as f:
        tx1 = f.readline()
        tx2 = f.readline()
    assert tx1 != tx2, "{} равно {}".format(tx1, tx2)


@When('закончили тест')
def step(context):
    context.browser.quit()
