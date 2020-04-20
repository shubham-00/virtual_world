from selenium import webdriver

driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\ChromeDriver\chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "' + name + '"]')
# user = driver.find_element_by_class_name('')
# driver.find_elements_by_xpath()

user.click()

msg_box = list(driver.find_element_by_class_name('_2S1VP'))[1]

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()




'''
css-18t94o4
css-1dbjc4n
r-1777fci
r-11cpok1
r-1ny4l3l
r-bztko3
r-lrvibr

like_button = driver.find_element_by_class_name('css-18t94o4')
like_button = driver.find_element_by_class_name('css-1dbjc4n')
like_button = driver.find_element_by_class_name('r-1777fci')
like_button = driver.find_element_by_class_name('r-11cpok1')
like_button = driver.find_element_by_class_name('r-1ny4l3l')
like_button = driver.find_element_by_class_name('r-bztko3')
like_button = driver.find_element_by_class_name('r-lrvibr')


'''