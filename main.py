from selenium import webdriver

chrome_webdriver_path = "C:\Chrome driver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_webdriver_path)

driver.get("https://www.python.org/")

event_time = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

for i in range(len(event_time)):
    events[i]={
        "time": event_time[i].text,
        "events": event_name[i].text,
    }
print(events)
driver.quit()