import glob
import os

from selenium import webdriver

dictCB = dict(Поиск='//*[@title="Поиск"]', email='//*[@name="email"]', заголовка='shadow-box__title')


def before_all(context):
    context.browser = webdriver.Firefox()

    files = glob.glob(os.path.join('.', 'screen', '*.png'))
    for s in files:
        os.remove(s)

    with open('genius_idea.txt', 'w+', encoding='utf-8') as f:
        f.write('')


def after_all(context):
    context.browser.quit()
