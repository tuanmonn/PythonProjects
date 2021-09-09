from selenium import webdriver

chrome_driver_path = "/Users/tuanmonn/Documents/chromedriver"
driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)

driver.quit()