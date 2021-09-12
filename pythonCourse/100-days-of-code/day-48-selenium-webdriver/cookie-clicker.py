from selenium import webdriver
import time

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes


chrome_driver_path = "/Users/tuanmonn/Documents/chromedriver"
driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Get the cookie item
cookie = driver.find_element_by_id("cookie")

# Get all the buy ids
part_of_name = "buy"
all_ids = driver.find_elements_by_css_selector('[id*="%s"]' % part_of_name)

# Create the lists
item_list = []
price_list = []

# Get the items' names and their prices:
for n in range(0,len(all_ids)-1):
    result = all_ids[n].text                                # get the text of each id
    get_list = result.split("-")                            # split the result for the name and the price
    get_item_name = get_list[0].strip()                     # get the item name
    price_and_text_list = get_list[1].split("\n")           # the price is stuck with the description so I split it to a list
    get_price = price_and_text_list[0].strip()              # get the price and strip the unnecessary space
    get_price_int = int(get_price.replace(",", ""))         # convert to integer (important)
    price_list.append(get_price_int)
    item_list.append(get_item_name)


# Function to click buy on the most expensive items
def buyItem(money):
    for n in range(len(price_list)-1,0,-1):
        if money > price_list[n]:
            click_item = driver.find_element_by_id(f"buy{item_list[n]}")
            click_item.click()
            break

game = True
while game:
    cookie.click()
    if time.time() > timeout:
        num_cookie = driver.find_element_by_id("money")

        # get and convert the num of cookies
        asset = num_cookie.text
        if "," in asset:
            asset = asset.replace(",", "")
        asset_num = int(asset)

        # buy the item
        buyItem(asset_num)

        # increase the time 5 more seconds
        timeout = time.time() + 5

    # stop after 5 mins
    if time.time() > five_min:
        game = False

cps = driver.find_element_by_id("cps")
print(cps.text)

driver.quit()