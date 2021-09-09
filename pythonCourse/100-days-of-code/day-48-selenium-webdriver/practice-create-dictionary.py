from pylint.checkers.typecheck import _
from selenium import webdriver

# set up selenium chrome driver
chrome_driver_path = "/Users/tuanmonn/Documents/chromedriver"
driver = webdriver.Chrome(executable_path= chrome_driver_path)

event_dict = {}

driver.get("https://www.python.org")
event_dates = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

# event_names.pop(0) # we don't need this if we narrow down to the anchor tag of the event name

for n in range(0,len(event_dates)):
    event_dict[n] = {
        "dates": event_dates[n].text,
        "name": event_names[n].text,
    }

print(event_dict)
driver.quit()