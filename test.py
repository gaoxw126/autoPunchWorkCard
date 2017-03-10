from selenium import webdriver
import time

check_in_list = [
    time.mktime(time.strptime("2017-03-08 19:50:00", "%Y-%m-%d %H:%M:%S")),
    time.mktime(time.strptime("2017-03-08 20:20:00", "%Y-%m-%d %H:%M:%S")),
    time.mktime(time.strptime("2017-02-23 9:30:00", "%Y-%m-%d %H:%M:%S")),
]
stop_time = time.mktime(time.strptime("2017-03-26 10:50:59", "%Y-%m-%d %H:%M:%S"))
user = ""
psw = ""

def do_check_in():
    #browser = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
    browser = webdriver.Chrome()
    browser.get("http://***.com")

    account = browser.find_element_by_id("username")
    passwd = browser.find_element_by_id("password")
    login = browser.find_element_by_class_name("formsubmit_btn")
    account.send_keys(user)
    passwd.send_keys(psw)
    login.click()

    try:
        guide_close = browser.find_element_by_class_name("step_close")
        guide_close.click()
    except Exception:
        pass
    check_in = browser.find_element_by_class_name("check-in")
    check_in.click()

    time.sleep(1)
    browser.close()

for check_in_time in check_in_list:
    while True:
        if time.time() >= stop_time:
            exit(0)

        if time.time() >= check_in_time :
            do_check_in()
            time.sleep(5)
            break

        time.sleep(5)

