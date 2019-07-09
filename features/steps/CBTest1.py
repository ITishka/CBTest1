# -- FILE: features/environment.py

from datetime import datetime

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from features.environment import dictCB


@Given('пользователь на странице "{url}"')
def step(context, url):
    context.browser.get(url)


@Then('отображается поле "{field}"')
def step(context, field):
    assert context.browser.find_element_by_xpath('//*[@title="{}"]'.format(field))


@Then('ввели в поле "{field}" "{text}"')
def step(context, field, text):
    # dictCB = dict(Поиск='//*[@title="Поиск"]',
    #               email='//*[@name="email"]')

    elem = context.browser.find_element_by_xpath(dictCB[field])
    elem.send_keys(text)
    elem.send_keys(Keys.RETURN)


@Then('дождались загрузки страницы "{page}"')
def step(context, page):
    WebDriverWait(context.browser, 5).until(EC.title_contains(page))


@When('нажали на "{textlink}"')
def step(context, textlink):
    elem = context.browser.find_element_by_partial_link_text(textlink)
    href = elem.get_attribute('href')
    context.browser.get(href)


@Then('вышло сообщение "{text}"')
def step(context, text):
    WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//div[text()="{}"]'.format(text))))


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
    tx = context.browser.find_element_by_class_name(dictCB[text]).text
    with open('genius_idea.txt', 'a') as f:
        f.write(tx + '\n')


@Then('сравнили запомненные тексты')
def step(context):
    with open('genius_idea.txt', 'r+') as f:
        tx1 = f.readline()
        tx2 = f.readline()
    assert tx1 != tx2, "{} равно {}".format(tx1, tx2)
