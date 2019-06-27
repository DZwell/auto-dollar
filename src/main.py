import os
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from months-list import months

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


def get_month():
    return current_month = months[datetime.now().month]




login(email, password)
get_expense_amount('cable')