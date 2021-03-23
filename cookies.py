from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

webdriver_path = "C:\Chrome driver\chromedriver.exe"
url = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(executable_path=webdriver_path)

driver.get(url)
# cookie = driver.find_element_by_css_selector("div #cookie")
cookie = driver.find_element_by_id("cookie")
items = driver.find_elements_by_css_selector("#store div")
items_id = [item.get_attribute("id") for item in items]


timeout = time.time() + 5
fiv_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_price = []

        #Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_price.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for i in range(len(item_price)):
            cookie_upgrades[item_price[i]] = items_id[i]

        #Counting the money element
        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(',',"")
        cookie_count = int(money)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    if time.time() > fiv_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break








