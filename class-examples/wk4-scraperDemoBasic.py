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

    # Find all elements with the class "event" (assuming event information is in elements with this class)
    event_elements = soup.find_all("tr")
    print(len(event_elements))

    # Iterate through the event elements and extract event information
    for event_element in event_elements:
        rows = event_element.find_all("td")
        for row in rows:
            event_data = event_element.find("td").text
            print(event_data)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

