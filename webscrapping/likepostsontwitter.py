from selenium import webdriver
from getpass import getpass
import time

email = input('Email: ')
password = getpass('Password: ')

driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\ChromeDriver\chromedriver.exe")
driver.get('https://twitter.com/login')

time.sleep(20)

email_box = driver.find_element_by_name('session[username_or_email]')
email_box.send_keys(email)

# time.sleep(5)

password_box = driver.find_element_by_name('session[password]')
password_box.send_keys(password)

# time.sleep(5)

login_button = driver.find_element_by_xpath('//div[@role = "button"]')
login_button.click()

time.sleep(20)

like_buttons = driver.find_elements_by_xpath('//div[@data-testid = "like"]')
print("Total Posts:", len(list(like_buttons)))
for like_button in list(like_buttons):
  time.sleep(5)
  try:
    like_button.click()
  except:
    pass

# time.sleep(5)

driver.close()
