import random
from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By
import string

from datetime import datetime

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

def random_word_generator(length):
    return "".join(random.choices(string.ascii_letters, k=length))+"Ad2"

def random_psswrd_generator(length):
    return "".join(random.choices(string.ascii_letters, k=length))+"Ae9"

def generate_html_report(lists):
    titles_of_tests = []
    states_of_tests = []
    durations_of_tests = []
    for li in lists:
        titles_of_tests.append(li[0])
        states_of_tests.append(li[1])
        durations_of_tests.append(li[2])

    html = f'''
        <html>
        <head>
          <title>Test Report</title>
        </head>
        <body>
          <h1>Test Report</h1>
          <br>
          <h3>{titles_of_tests[0]}</h3>
          <p>
            <span>Duration : {durations_of_tests[0]}</span>
          </p>
          <p>
            <span style="background-color:{"#71ef09" if states_of_tests[1]=="True" else "#d30606"}">Test state : {"passed" if states_of_tests[0]=="True" else "failed"}</span>
          </p>
          <br>
          <h3>{titles_of_tests[1]}</h3>
          <p>
            <span>Duration : {durations_of_tests[1]}</span>
          </p>
          <p>
            <span style="background-color:{"#71ef09" if states_of_tests[1]=="True" else "#d30606"}">Test state : {"passed" if states_of_tests[1]=="True" else "failed"}</span>
          </p>
          <br>
          <h3>{titles_of_tests[2]}</h3>
          <p>
            <span>Duration : {durations_of_tests[2]}</span>
          </p>
          <p>
            <span style="background-color:{"#71ef09" if states_of_tests[1]=="True" else "#d30606"}">Test state : {"passed" if states_of_tests[2]=="True" else "failed"}</span>
          </p>
          <br>
          <h3>{titles_of_tests[3]}</h3>
          <p>
            <span>Duration : {durations_of_tests[3]}</span>
          </p>
          <p>
            <span style="background-color:{"#71ef09" if states_of_tests[1]=="True" else "#d30606"}">Test state : {"passed" if states_of_tests[3]=="True" else "failed"}</span>
          </p>
        </body>
        </html>
    '''
    date_now = datetime.now().strftime("%d%m%y_%H%M%S")
    file_path = f"html_reports/html_report_{date_now}.html"
    with open(file_path, "w") as f:
        f.write(html)


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
sign_up_button = "/html/body/app-root/div/app-header/header/nav/div/div[1]/a[3]"
first_name_input = "/html/body/app-root/div/app-sign-up-page/div/mat-card/div/form/p[1]/mat-form-field/div/div[1]/div[3]/input"
first_name_random = random_word_generator(6)
last_name_input = "/html/body/app-root/div/app-sign-up-page/div/mat-card/div/form/p[2]/mat-form-field/div/div[1]/div[3]/input"
last_name_random = random_word_generator(10)
mail_input_sign_up = "/html/body/app-root/div/app-sign-up-page/div/mat-card/div/form/p[3]/mat-form-field/div/div[1]/div[3]/input"
mail_sign_up = ".".join([first_name_random, last_name_random])+"@test.com"
psswrd_input_sign_up = "/html/body/app-root/div/app-sign-up-page/div/mat-card/div/form/p[4]/mat-form-field/div/div[1]/div[3]/input"
psswrd_sign_up = random_psswrd_generator(9)
sign_up_button_page2 = "/html/body/app-root/div/app-sign-up-page/div/mat-card/div/form/p[5]/button"
sign_up_confirmation_pop_up_message = "/html/body/div[2]/div/div/snack-bar-container/div/div/simple-snack-bar/span"
        #test
def tests_account_creation(browser):
    time = datetime.now()
    test_goal = "Account creation test"
    #page1
    click_on_element(browser, sign_up_button)
    #page2
    sleep(2)
    type_text_in_element(browser, first_name_random, first_name_input)
    type_text_in_element(browser, last_name_random, last_name_input)
    type_text_in_element(browser, mail_sign_up ,mail_input_sign_up)
    type_text_in_element(browser, psswrd_sign_up, psswrd_input_sign_up)
    click_on_element(browser, sign_up_button_page2)
    #popup
    sleep(2)
    pop_up_message = browser.find_element(By.XPATH, sign_up_confirmation_pop_up_message).get_attribute("innerHTML")
    try:
        assert "Cool! Now try to log in" in pop_up_message
        ok_message(test_goal)
        return [test_goal, str(True), str(datetime.now()-time)]
    except AssertionError:
        ko_message(test_goal)
        return [test_goal, str(False), str(datetime.now()-time)]
#
    #2
        #vars
login_button = "body > app-root > div > app-header > header > nav > div > div:nth-child(1) > a:nth-child(2)"
mail_input_full_XPATH = '/html/body/app-root/div/app-log-in-page/div/mat-card/div/form/p[1]/mat-form-field/div/div[1]/div[3]/input'
mail = mail_sign_up
psswrd_input_full_XPATH = "/html/body/app-root/div/app-log-in-page/div/mat-card/div/form/p[2]/mat-form-field/div/div[1]/div[3]/input"
psswrd = psswrd_sign_up
log_in_button_page2 = "/html/body/app-root/div/app-log-in-page/div/mat-card/div/form/p[3]/button"
my_heroes_title_in_homepage = "#left > h2"
        #test
def tests_login(browser):
    time = datetime.now()
    test_goal = "Login test"
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
        return [test_goal, str(True), str(datetime.now() - time)]
    except AssertionError:
        ko_message(test_goal)
        return [test_goal, str(False), str(datetime.now() - time)]
#
    #3
        #vars
hero_name_input = "/html/body/app-root/div/app-my-heroes-page/div[2]/div[1]/form/mat-form-field[1]/div/div[1]/div/input"
alter_ego_input = "/html/body/app-root/div/app-my-heroes-page/div[2]/div[1]/form/mat-form-field[2]/div/div[1]/div/input"
create_hero_button = "/html/body/app-root/div/app-my-heroes-page/div[2]/div[1]/form/button"
create_hero_button = "/html/body/app-root/div/app-my-heroes-page/div[2]/div[1]/form/button"
creation_pop_up_message = "/html/body/div[2]/div/div/snack-bar-container/div/div/simple-snack-bar"
        #test
def tests_hero_creation(browser):
    time = datetime.now()
    test_goal = "Hero creation test"
    name = "".join(random.choices(string.ascii_letters, k=9))
    alter_ego = "".join(random.choices(string.ascii_letters, k=9))
    #page_1
    type_text_in_element(browser, f"super {name}", hero_name_input)
    type_text_in_element(browser, f"cool {alter_ego}", alter_ego_input)
    click_on_element(browser, create_hero_button)
    #popup
    sleep(2)
    pop_up_text = browser.find_element(By.XPATH, creation_pop_up_message).get_attribute("innerHTML")
    try:
        assert "Hero created" in pop_up_text
        ok_message(test_goal)
        return [test_goal, str(True), str(datetime.now() - time)]
    except AssertionError:
        ko_message(test_goal)
        return [test_goal, str(False), str(datetime.now() - time)]
#
    #4
        #vars
delete_button = "/html/body/app-root/div/app-my-heroes-page/div[1]/div/mat-list/mat-list-item[1]/span/div/mat-icon"
confirm_deletion_button = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-hero-remove/mat-dialog-actions/button[2]"
deletion_popup_message = "/html/body/div[2]/div/div/snack-bar-container/div/div/simple-snack-bar/span"
        #test
def tests_hero_deletion(browser):
    time = datetime.now()
    test_goal = "Hero deletion test"
    #page1
    click_on_element(browser, delete_button)
    #popup prompt
    click_on_element(browser, confirm_deletion_button)
    #popup message
    sleep(2)
    popup_deletion_message = browser.find_element(By.XPATH, deletion_popup_message).get_attribute("innerHTML")
    try:
        assert "Hero removed" in popup_deletion_message
        ok_message(test_goal)
        return [test_goal, str(True), str(datetime.now() - time)]
    except AssertionError:
        ko_message(test_goal)
        return [test_goal, str(False), str(datetime.now() - time)]
#

#main
def main():
    with webdriver.Chrome() as browser:
        browser.get("https://ismaestro.github.io/angular-example-app/")
        #0
        verify_title(browser)
        #1
        sleep(2)
        test_1_return_list = tests_account_creation(browser)
        #2
        sleep(2)
        test_2_return_list = tests_login(browser)
        #3
        sleep(2)
        test_3_return_list = tests_hero_creation(browser)
        #4
        sleep(2)
        test_4_return_list = tests_hero_deletion(browser)

        all_test_return_lists = [test_1_return_list, test_2_return_list, test_3_return_list, test_4_return_list]
        #report
        generate_html_report(all_test_return_lists)



        #end
        sleep(20)

#launch
if __name__ == '__main__':
    main()

