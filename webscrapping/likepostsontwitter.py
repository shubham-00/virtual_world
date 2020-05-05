from selenium import webdriver
from getpass import getpass
import time
import random

# email = input('Email: ')
# password = getpass('Password: ')

email = input('Enter email: ')
password = getpass('Enter pasword: ')

driver = webdriver.Chrome(
    r"C:\Program Files (x86)\Google\Chrome\ChromeDriver\chromedriver.exe")  # 
driver.get('https://twitter.com/login')

time.sleep(random.randint(3, 10))

email_box = driver.find_element_by_name('session[username_or_email]')
email_box.send_keys(email)

# time.sleep(5)

password_box = driver.find_element_by_name('session[password]')
password_box.send_keys(password)

# time.sleep(5)

login_button = driver.find_element_by_xpath('//div[@role = "button"]')
login_button.click()

time.sleep(random.randint(3, 10))

button = driver.find_element_by_xpath('//a[@href = "/explore"]')
button.click()

time.sleep(random.randint(3, 6))

# button = driver.find_element_by_xpath('//*[text()[contains(., "Fun")]]')
# button = button.find_element_by_xpath('..')
# button = button.find_element_by_xpath('..')
# button.click()

# button = driver.find_elements_by_class_name('css-4rbku5 css-18t94o4 css-1dbjc4n r-1awozwy r-oucylx r-rull8r r-wgabs5 r-1loqt21 r-6koalj r-eqz5dr r-16y2uox r-1777fci r-1ny4l3l r-1oqcu8e r-o7ynqc r-6416eg')
# button = driver.find_elements_by_class_name('css-901oao')[27]
# button.click()

# quit()

print(button.__dir__())

refresh = 0
scroll = 100

while True:
    refresh += 1
    if refresh == random.randint(7, 13):
        refresh = 0
        driver.refresh()
    try:
	    driver.execute_script("window.scroll(0, {})".format(scroll))
	    scroll += 100
    except:
	    scroll = 100
    time.sleep(random.randint(3, 10))
    like_buttons = driver.find_elements_by_xpath(
        '//div[@data-testid = "like"]')
    print("Total Posts:", len(list(like_buttons)))
    for like_button in list(like_buttons):
        time.sleep(random.randint(3, 10))
        try:
            like_button.click()
        except:
            pass

time.sleep(random.randint(3, 10))

driver.close()
