# Project purpose
# Scrape booking.com for the hotels that match my requirement
# Add them to a Google Form -> excel sheet so my team can vote on it

from selenium import webdriver
import fill_form

# user input
link_input = input("Paste your link here: ")
place_input = input("Your destination: ")
budget_per_person = int(input("Input the budget for each person per night: "))
group_num = int(input("How many people are in your group?: "))
night = int(input("How many nights is your group staying?: "))
budget_input = budget_per_person * group_num * night

# install driver
chrome_driver_path = "/Users/tuanmonn/Documents/chromedriver"
driver = webdriver.Chrome(executable_path= chrome_driver_path)

# lists of all hotels
hotel_names = []
hotel_prices = []
hotel_links = []

# lists of affordable hotels
affordable_hotel_prices = []
affordable_hotel_names = []
affordable_hotel_links = []

# get data from site
driver.get(link_input)

# get hotel names, prices, and links
hotels = driver.find_elements_by_class_name("sr-hotel__name")
prices = driver.find_elements_by_class_name("prco-valign-middle-helper")
links = driver.find_elements_by_css_selector(".js-sr-hotel-link.hotel_name_link.url")

# add data into lists
for n in range(0,len(hotels)-1):
    # hotel
    hotel_names.append(hotels[n].text)

    # price
    price = prices[n].text
    price = price.split()[1]
    price = int(price.replace(".",""))
    hotel_prices.append(price)

    # link
    link = links[n].get_attribute("href")               # I used .text but that didn't return the link, should be href
    hotel_links.append(link)

# select hotels that are within our budget, add to new list
for n in range(0, len(hotel_prices)-1):
    if hotel_prices[n] < budget_input:
        affordable_hotel_prices.append(hotel_prices[n])
        affordable_hotel_names.append(hotel_names[n])
        affordable_hotel_links.append(hotel_links[n])

# Fill form
for n in range(0, len(affordable_hotel_names)-1):
    fill_form.fill_form(affordable_hotel_names[n],affordable_hotel_prices[n],affordable_hotel_links[n],place_input)

driver.quit()

