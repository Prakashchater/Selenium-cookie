from selenium import webdriver
from selenium.webdriver.common.keys import Keys

webdriver_path = "C:\Chrome driver\chromedriver.exe"
url = "http://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome(executable_path=webdriver_path)

driver.get(url)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Prakash")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Chater")
email = driver.find_element_by_name("email")
email.send_keys("xyz@gmail.com")
sign_up = driver.find_element_by_tag_name("button") #or
sign = driver.find_element_by_css_selector("form button")
sign.click()


