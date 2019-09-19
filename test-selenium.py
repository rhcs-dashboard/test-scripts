#!/usr/bin/python

from selenium import webdriver
options = webdriver.FirefoxOptions()
options.add_argument('-headless')

un = "admin"
pwd = "admin"

# Start selenium with the configured binary.
browser = webdriver.Firefox(executable_path='/usr/bin/geckodriver', firefox_options=options)
browser.implicitly_wait(30)
browser.maximize_window()

# Access the ceph-dashboard url
browser.get('http://10.70.42.252:11001')
assert "Ceph" in browser.title
#browser.save_screenshot('test.png')

un_field = browser.find_element_by_name("username")
pw_field = browser.find_element_by_name("password")

un_field.send_keys(un)
pw_field.send_keys(pwd)

button = browser.find_element_by_name("loginForm")
button.submit()

print('Login Successful')

element = browser.find_element_by_class_name("info-group-title").text
assert "Status" in element

element = browser.find_element_by_class_name("card-title m-4").text
assert "Cluster statuse" in element

#element = browser.find_element_by_class_name("ng-star-inserted").text
#print(element)

browser.quit()

