# Fandom Frenzy using Flask

## Introduction
In this assignment, you will use the Flask library in Python to create a web application called "Fandom Frenzy." The application will serve as a fan community website dedicated to a particular film, TV show, video game, or other fictional universe. You will build multiple routes/pages to showcase various aspects of the fandom, such as discussions, fan art, character profiles, and more.

## Task
Your task is to build the Fandom Frenzy web application using Flask. Each route/page should represent a different section or feature of the fan community website.

## Instructions

1. **Install Flask**: If you don't have Flask installed, use the following command to install it:
   ```
   pip install flask
   ```

2. **Create a new Python script**: Create a new Python script named `fandom_frenzy.py`.

3. **Import the necessary modules**: Import the necessary modules in your Python script:
   ```python
   from flask import Flask, render_template
   ```

4. **Create an instance of the Flask class**: Create an instance of the Flask class in your Python script:
   ```python
   app = Flask(__name__)
   ```

5. **Define multiple routes for your application**: Define multiple routes for your application in your Python script. Each route will represent a different section or feature of the fan community website:
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

6. **Define view functions for each route**: Define view functions for each route in your Python script. Each view function will render the corresponding HTML template:
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

7. **Create HTML templates for each page**: Create HTML templates for each page in your Flask application. Each template will represent a different section or feature of the fan community website. Customize the templates to match the design and theme of the fan community website.

8. **Test your application**: Run the Flask application and test it by navigating to different routes in your web browser.

---

Follow these instructions to complete the Fandom Frenzy using Flask assignment. Customize the content, design, and features of your fan community website to cater to the chosen fictional universe and create an engaging experience for fans.

Best of luck with your assignment! Submit a link to the index (main) page using the submission dropbox in Webcourses.
