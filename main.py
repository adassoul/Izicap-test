import random
from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By
import string
waiting_period = 20

def ok_message(message):
    print(f"------Okay!------ : {message} passed")
def ko_message(message):
    print(f"------Knocked Out------ : {message} didn't pass...")

def click_on_element(browser, selector, method="full_xpath"):
    if method == "css_selector":
        browser.find_element(By.CSS_SELECTOR, selector).click()
    elif method == "full_xpath" or method == "xpath":
        browser.find_element(By.XPATH, selector).click()
def type_text_in_element(browser, text, selector, method="full_xpath"):
    if method == "css_selector":
        browser.find_element(By.CSS_SELECTOR, selector).send_keys(text)
    elif method == "full_xpath" or method == "xpath":
        browser.find_element(By.XPATH, selector).send_keys(text)

#tests
#
    #0
def verify_title(browser):
    test_goal = "title verif"
    title = browser.title
    try:
        assert "App title" in title
        ok_message(test_goal)
    except AssertionError:
        ko_message(test_goal)
#
    #1
        #vars
login_button = "body > app-root > div > app-header > header > nav > div > div:nth-child(1) > a:nth-child(2)"
mail_input_full_XPATH = '/html/body/app-root/div/app-log-in-page/div/mat-card/div/form/p[1]/mat-form-field/div/div[1]/div[3]/input'
mail = "aymane.dassouli@gmail.com"
psswrd_input_full_XPATH = "/html/body/app-root/div/app-log-in-page/div/mat-card/div/form/p[2]/mat-form-field/div/div[1]/div[3]/input"
psswrd = "aymaneAa22"
log_in_button_page2 = "/html/body/app-root/div/app-log-in-page/div/mat-card/div/form/p[3]/button"
my_heroes_title_in_homepage = "#left > h2"
        #test
def tests_login(browser):
    test_goal = "login test"
    #page_1
    click_on_element(browser, login_button, "css_selector")
    #page_2
    sleep(2)
    type_text_in_element(browser, mail, mail_input_full_XPATH, "full_xpath")
    type_text_in_element(browser, psswrd, psswrd_input_full_XPATH, "full_xpath")
    click_on_element(browser, log_in_button_page2, "full_xpath")
    #page3
    sleep(2)
    my_heroes_title = browser.find_element(By.CSS_SELECTOR, my_heroes_title_in_homepage).get_attribute("innerHTML")
    try:
        assert "My heroes" in my_heroes_title
        ok_message(test_goal)
    except AssertionError:
        ko_message(test_goal)
#
    #2
        #vars
hero_name_input = "/html/body/app-root/div/app-my-heroes-page/div[2]/div[1]/form/mat-form-field[1]/div/div[1]/div/input"
alter_ego_input = "/html/body/app-root/div/app-my-heroes-page/div[2]/div[1]/form/mat-form-field[2]/div/div[1]/div/input"
create_hero_button = "/html/body/app-root/div/app-my-heroes-page/div[2]/div[1]/form/button"
create_hero_button = "/html/body/app-root/div/app-my-heroes-page/div[2]/div[1]/form/button"

pop_up_xpath = "/html/body/div[2]/div/div/snack-bar-container/div/div/simple-snack-bar" #notsure
        #test
def tests_hero_creation(browser):
    test_goal = "hero creation test"
    name = "".join(random.choices(string.ascii_letters, k=9))
    alter_ego = "".join(random.choices(string.ascii_letters, k=9))
    #page_1
    type_text_in_element(browser, f"super {name}", hero_name_input)
    type_text_in_element(browser, f"cool {alter_ego}", alter_ego_input)
    click_on_element(browser, create_hero_button)
    sleep(2)
    pop_up_text = browser.find_element(By.XPATH, pop_up_xpath).get_attribute("innerHTML")
    try:
        assert "Hero created" in pop_up_text
        ok_message(test_goal)
    except AssertionError:
        ko_message(test_goal)

#main
def main():
    with webdriver.Chrome() as browser:
        browser.get("https://ismaestro.github.io/angular-example-app/")
        #0
        verify_title(browser)
        #1
        sleep(2)
        tests_login(browser)
        #2
        sleep(2)
        tests_hero_creation(browser)

        #end
        sleep(5)


#launch
if __name__ == '__main__':
    main()

