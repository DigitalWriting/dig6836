import requests
from bs4 import BeautifulSoup

# URL of the news article you want to scrape
url = "https://www.example.com/news/article1"  # Replace with the actual URL

# Function to scrape title and first paragraph from a news article
def scrape_news_article(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract the title of the article
            title = soup.title.string

            # Find the first paragraph (you can adjust the selector as needed)
            first_paragraph = soup.find("p").text

            return title, first_paragraph
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

# Call the function and store the results
article_title, article_paragraph = scrape_news_article(url)

# Print the results
print("Title of the article:", article_title)
print("First paragraph of the article:")
print(article_paragraph)
