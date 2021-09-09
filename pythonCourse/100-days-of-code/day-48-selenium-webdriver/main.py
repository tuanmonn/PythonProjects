from selenium import webdriver

# set up selenium chrome driver
chrome_driver_path = "/Users/tuanmonn/Documents/chromedriver"
driver = webdriver.Chrome(executable_path= chrome_driver_path)

# find element by id
# driver.get("https://www.amazon.com/Acer-AN515-55-53E5-i5-10300H-GeForce-Keyboard/dp/B092YHJGMN/ref=lp_16225007011_1_5")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# find elements by name
# driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
#
# find elements by class
# driver.get("https://www.python.org")
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# find elements by css selector -> find sth without a specific name or class
# driver.get("https://www.python.org")
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a") #find any anchor tag inside the class documentation-widget
# print(documentation_link.text)


# find element by a path
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)




# driver.close()          # close the active tab
driver.quit()           # quit the entire browser