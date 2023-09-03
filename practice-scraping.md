**Practice Exercise: Basic Web Scraping with BeautifulSoup**

**Objective:** In this exercise, you will practice using BeautifulSoup to scrape information from a webpage. You will scrape the title and the first paragraph of a news article from a website.

**Instructions:**

1. Choose a news website or any webpage of your choice that contains news articles. Ensure that the website allows web scraping and does not violate its terms of service.

2. Install the required libraries if you haven't already. You'll need `requests` to fetch the webpage and `BeautifulSoup` to parse it. You can install them using pip:

   ```python
   pip install requests beautifulsoup4
   ```

3. Write a Python script that does the following:

   - Use the `requests` library to fetch the webpage's HTML content.
   - Create a BeautifulSoup object to parse the HTML content.
   - Extract the title of the news article and store it in a variable.
   - Extract the text of the first paragraph of the article and store it in another variable.

4. Print the extracted title and the first paragraph.

5. Test your code with different news articles from the chosen website to ensure it works correctly.

**Bonus (Optional):**

If you want to challenge yourself further, you can consider these additional tasks:

- Create a function that takes a URL as input and returns the title and first paragraph of the news article.
- Modify your code to scrape and store multiple news articles from the same webpage in a structured format, such as a list of dictionaries.

**Note:** Always respect the website's terms of service and robots.txt file when web scraping, and be mindful of the frequency and volume of your requests to avoid overloading the server.
