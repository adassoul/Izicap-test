from time import sleep
from selenium import webdriver

waiting_period = 20

def ok_message(message):
    print(f"------Okay!------ : {message} passed")

def ko_message(message):
    print(f"------Knocked Out------ : {message} didn't pass...")



def verify_title(browser):
    test_goal = "title verif"
    title = browser.title
    try:
        assert "App title" in title
        ok_message(test_goal)
    except AssertionError:
        ko_message(test_goal)


def main():
    with webdriver.Chrome() as browser:
        browser.get("https://ismaestro.github.io/angular-example-app/")
        verify_title(browser)
        sleep(waiting_period)


if __name__ == '__main__':
    main()

