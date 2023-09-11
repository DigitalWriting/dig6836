import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to a webpage and get its HTML content
url = "https://example.com"
response = requests.get(url)
html_content = response.content

# Step 2: Create a Beautiful Soup object from the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Step 3: Access elements using tag names
title = soup.title  # Access the <title> tag
print("Page title:", title.text)  # Print the text content of the title tag

# Step 4: Access elements using CSS selectors
first_paragraph = soup.select_one("p")  # Access the first <p> tag
print("First paragraph:", first_paragraph.text)

# Step 5: Access elements using class names
highlighted_elements = soup.select(".highlight")  # Access elements with the class "highlight"
for element in highlighted_elements:
    print("Highlighted element:", element.text)

# Step 6: Access elements using ID
main_heading = soup.select_one("h1")  # Access the element with the ID "main-heading"
print("Main heading:", main_heading.text)

# Step 7: Access parent, sibling, and child elements
first_paragraph = soup.select_one("p")
parent_div = first_paragraph.parent  # Access the parent <div> element
next_sibling_paragraph = first_paragraph.next_sibling  # Access the next sibling <p> element
first_child_of_div = parent_div.contents[0]  # Access the first child element of the parent <div>

# Step 8: Extract attributes and navigate to links
link = soup.select_one("a")
link_text = link.text  # Get the text content of the link
link_url = link["href"]  # Get the value of the "href" attribute
print("Link text:", link_text)
print("Link URL:", link_url)

# Step 9: Extract all links on the page
all_links = soup.find_all("a")
for link in all_links:
    link_text = link.text
    link_url = link["href"]
    print("Link text:", link_text)
    print("Link URL:", link_url)
