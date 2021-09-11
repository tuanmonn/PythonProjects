from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/tuanmonn/Documents/chromedriver"
driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Tuan")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Nguyen")

email = driver.find_element_by_name("email")
email.send_keys("haha@gmail.com")

sign_up_btn = driver.find_element_by_tag_name("button")
# another way
# sign_up_btn = driver.find_element_by_css_selector("form button")
sign_up_btn.click()
