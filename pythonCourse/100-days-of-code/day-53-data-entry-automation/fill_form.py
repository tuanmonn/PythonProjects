from selenium import webdriver

def fill_form(hotel_name, hotel_price, hotel_link, hotel_tag):
    # install driver
    chrome_driver_path = "/Users/tuanmonn/Documents/chromedriver"
    new_driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # open google form
    new_driver.get("https://forms.gle/9y3D7z4qN3ELCVQZ8")
    hotel_form = new_driver.find_elements_by_css_selector(".quantumWizTextinputPaperinputInput.exportInput")

    # fill in the form
    hotel_form[0].send_keys(hotel_name)
    hotel_form[1].send_keys(hotel_price)
    hotel_form[2].send_keys(hotel_link)
    hotel_form[3].send_keys(hotel_tag)

    # submit result
    submit = new_driver.find_element_by_css_selector(".appsMaterialWizButtonPaperbuttonContent.exportButtonContent")
    submit.click()

    new_driver.quit()
