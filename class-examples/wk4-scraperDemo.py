import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "http://www.rudymcdaniel.com/test/arts-test.html"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all elements with the class "event" 
    event_elements = soup.find_all("div", id="event")

     # Iterate through the event elements and extract event information
    for event_element in event_elements:
        
        # Extract event name and other information
        event_name = event_element.find("td", class_="event_name").text
        event_date = event_element.find("td", class_="event_date").text
        event_location = event_element.find("td", class_="location").text
        event_notes = event_element.find("a")['href']

        # Print details for each event
        print(f"{event_name}\nDate: {event_date}")
        print(f"Location: {event_location}")
        print(f"Notes: {event_notes}\n")
        
    # Now, list information on partnerships
    partner_elements = soup.find_all("li")
    
    print(" -- Arts Partner Organizations -- ")
    
    for partner_element in partner_elements:
        print(partner_element.text)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
