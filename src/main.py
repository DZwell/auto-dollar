import os
import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import months

email = os.environ['ED_EMAIL']
password = os.environ['ED_PASSWORD']

chrome_options = Options()
# chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://everydollar.id.ramseysolutions.net/sign-in?scope=openid%20profile%20email&response_type=code&client_id=everydollar&redirect_uri=https%3A%2F%2Fwww.everydollar.com%2Fapp%2Fauth&state=eyJmcm9tIjp7InBhdGhuYW1lIjoiL2J1ZGdldCJ9fQ&code_challenge=OTMnsDl29IHFOdd4MzyR93iAslsKO_O0Ea5fnBFRWlk&code_challenge_method=S256')


def login(email, password):
    browser.find_element_by_xpath('//input[@type="email"]').send_keys(email)
    browser.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    browser.find_element_by_xpath('//button[@type="submit"]').click()


def get_expense_amount(expense):
    expense_file = open('expenses.json', 'r')
    expense_file.seek(0)
    expenses = json.load(expense_file)
    amount = expenses[expense]
    expense_file.close()
    return amount


def get_next_month():
    return months[datetime.now().month]


def click_new_month():
    next_month = get_next_month()
    click_month_selector = "document.getElementsByClassName('BudgetNavigation-date')[0].click()"
    browser.execute_script(click_month_selector)
    time.sleep(1)
    browser.find_elements_by_class_name('BudgetNavigation-date')[0].click()
    browser.find_element_by_xpath(f'//div[text()={next_month}]').click()
    browser.find_element_by_id('Budget_startPlanning').click()




login(email, password)
click_new_month()
get_expense_amount('cable')