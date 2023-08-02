# Fandom Frenzy using Flask

## Introduction
In this assignment, you will use the Flask library in Python to create a web application called "Fandom Frenzy." The application will serve as a fan community website dedicated to a particular film, TV show, video game, or other fictional universe. You will build multiple routes/pages to showcase various aspects of the fandom, such as discussions, fan art, character profiles, and more.

## Task
Your task is to build the Fandom Frenzy web application using Flask. Each route/page should represent a different section or feature of the fan community website.

## Instructions

1. **Import necessary modules**: Before proceeding, make sure you have access to Google Colab. In the first code cell of your Jupyter notebook, import the necessary modules:
   ```python
   from flask import Flask, render_template
   ```

2. **Install and run ngrok (optional)**: Since Google Colab doesn't provide public URLs for hosted Flask applications, you can use ngrok to expose the local server to the internet. Install and run ngrok using the following code cell:
   ```python
   !pip install pyngrok
   from pyngrok import ngrok
   ```

3. **Create an instance of the Flask class**: In the next code cell, create an instance of the Flask class:
   ```python
   app = Flask(__name__)
   ```

4. **Define multiple routes for your application**: Define multiple routes for your application in subsequent code cells. Each route will represent a different section or feature of the fan community website:
   - Route 1: Home page
     - URL: `/`
     - Description: This page will serve as the landing page for your Fandom Frenzy application. It should provide an overview of the fandom, introduce the fictional universe, and display recent community activities.
   - Route 2: Discussions
     - URL: `/discussions`
     - Description: This page should showcase discussions related to the fictional universe. Users should be able to create new discussion threads, view existing discussions, and participate in conversations.
   - Route 3: Fan Art
     - URL: `/fanart`
     - Description: This page should feature fan-created artwork inspired by the fictional universe. Users can submit their own fan art, view a gallery of artwork, and interact with the artists.
   - Route 4: Character Profiles
     - URL: `/characters`
     - Description: This page should provide detailed profiles of characters from the fictional universe. Users can explore different characters, learn about their backstories, abilities, and relationships.
   - Route 5: Events and Conventions
     - URL: `/events`
     - Description: This page should list upcoming events, conventions, or meetups related to the fandom. Users can view event details, RSVP, and discuss event-related topics.
   - Feel free to add more routes/pages to incorporate additional features of the fan community website.

5. **Define view functions for each route**: Define view functions for each route in the subsequent code cells. Each view function will render the corresponding HTML template:
   - Create a function for the home page route:
     ```python
     @app.route('/')
     def index():
         # Add code to display content related to the fandom and recent activities
         return render_template('index.html')
     ```

   - Create view functions for each route:
     ```python
     @app.route('/discussions')
     def discussions():
         # Add code to display discussions
         return render_template('discussions.html')

     @app.route('/fanart')
     def fanart():
         # Add code to display fan art
         return render_template('fanart.html')

     @app.route('/characters')
     def characters():
         # Add code to display character profiles
         return render_template('characters.html')

     @app.route('/events')
     def events():
         # Add code to display events and conventions
         return render_template('events.html')
     ```

   - Remember to add more view functions for additional routes/pages.

6. **Create HTML templates for each page**: Create HTML templates for each page in your Google Colab environment. Each template will represent a different section or feature of the fan community website. Customize the templates to match the design and theme of the fan community website.

7. **Run the Flask application using ngrok**: To expose the Flask application to the internet, run the following code in a separate code cell:
   ```python
   # Run Flask app using ngrok to expose the local server to the internet
   app_url = ngrok.connect(port=5000)
   app.run(port=5000)
   ```

8. **Access the Fandom Frenzy application**: After running the ngrok code cell, the application will be accessible through the generated public URL provided by ngrok. You can find the URL in the output of the code cell.

9. **Test and submit**: Test your Fandom Frenzy web application by navigating to different routes using the public URL provided by ngrok. Ensure that all features and sections of the website work as expected. Once you are satisfied, you can submit your Jupyter notebook containing the completed assignment.

---

Follow these instructions to complete the Fandom Frenzy using Flask assignment in Google Colab and Jupyter notebook format. Customize the content, design, and features of your fan community website to cater to the chosen fictional universe and create an engaging experience for fans.

Best of luck with your assignment!
