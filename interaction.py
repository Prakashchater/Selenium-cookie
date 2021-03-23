from selenium import webdriver

driver_path = "C:\Chrome driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


# article = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')


article = driver.find_element_by_css_selector("#articlecount a")
print(article.text)





driver.quit()