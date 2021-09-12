# Project description

## Background
Our company organizes field trips every few months, and I'm often in charge of finding the hotels.

I want to create a central place (a Google Sheet) which contains the hotel name, its price, its link so everyone in my company can vote.

## High-level
- Scrape all hotels that match our requirements on Booking.com.
- Input those hotels' information into a Google Form, which is linked to a Google Sheet.

## Implementation
- I went to Booking.com, filter the location, the date, the number of people, the number of hotel stars
- Then I get the link pointing to the result place.
- The python program will ask for the link, some basic information like the destination, budget for each person... 
- Then it will auto scrape the data from the result page and fill in the Google Form.

## Future improvement(s)
- The user doesn't need to manually go to Booking.com and fill in all the requirements. The program should ask them this information and then get the result's link.

