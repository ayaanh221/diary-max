# Ayaan's cookbook
One or two paragraphs providing an overview of your project.
My project is an online cookbook where you can store recipes that you have create your self. You are able to add images methods , ingredients and many more thing. Once you have stored and saved a recipe of your choice you are able to edit and delete a recipe that you have already created, you can do all of this with easy access.

### Demo
[demo]( http://diary-max.herokuapp.com/get_tasks)
## UX
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.
[WIREFRAMES WOULD BE FOUND HERE]( https://balsamiq.cloud/s38zvoe/pe6k8yu)

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

The user's requirements are:

1. As a user I want to be able to add recipes
2. As a user I want to be able to get a confirmation that i added a recipe
3. As a user i want to see the recipe i added
4. As a user I want to be able to delete and edit the recipe i previously made

# Features
### Existing Features

This web application   allows users to store and access cooking recipes very easily. It is both fullstack and backend web application  that adds  all the CRUD (Create, Read, Update, Delete) functionality directly to a database hosted in the cloud on Heroku platform as a service. 
It allows users to do the following:
Add recipe-  once you fill out the add recipe form and you click on the submit recipe button it directly store the recipe in the recipe page which has it own uniqe layout.
My Recipes- this would allow you to view a all the recipes submitted by the current user that filled out the add recipe form.
### Features Left to Implement
1. I would like to add  a recipe planner where you would be able to add a recipe and a day you want to cook it, when the day arrives you would get a text message reminding you.
2. Dietary
# Technologies Used
 I have used the following  technologies:
HTML, CSS, JavaScript Python, front end from Materialize Full Stack Micro Framework Flask, SQL -relational database management system , pymongo
JQuery
The project uses JQuery to simplify DOM manipulation.
### Testing
I have tested all of the CRUD functionallties and they all .
I have tested the responsiveness of the app and made sure it works on diffrent screen sizes i have tested it with the following sizes and they all work and it is very easy to maneuver around it:-
1. Iphone x  - 375 x 812
2. Ipad - 768 x 1024
3. laptop - 1280 x 800


Try and submit a recipe and you would get a message that says 'recipe submitted'
During the testing i have came acorss my delete and edit button was sending me to the wrong link however i managed to fix it buy changing the way i wrote my href.



# Deployment
1. The requirements.txt and Procfile must exist: pip3 freeze --local requirements.txt echo web: python app.py > Procfile
2.Create Heroku App, Select Postgres add-on, download Heroku CLI toolbelt, login to heroku (Heroku login), git init, connect git to heroku (heroku git remote -a ), git add ., git commit, git push heroku master.
3.heroku ps:scale web=1
4.In heroku app settings set the config vars to add DATABASE_URL, IP and PORT

# Credits
### Content
1. The recipes in my recipes was taken from [Recipe Website BBC](https://www.bbc.co.uk/food/recipes)
2. I used this viedo to gain my knowledge in understand PHP CRUD in depth
[PHP CRUD Tutorial with MySQL](https://www.youtube.com/watch?v=3xRMUDC74Cw)
3. I frequently used [w3schools](https://www.w3schools.com/)
4. I used [Materialize](https://materializecss.com/) &[Build A Travel Agency Theme With Materialize CSS 1.0.0](https://www.youtube.com/watch?v=MaP3vO-vEsg&list=LLvkm_Fx2R6CFvKmjWx5TZHA&index=10&t=0s
for  my front end development.



### Media
The photos used in this site were obtained from  from [Recipe Website BBC](https://www.bbc.co.uk/food/recipes)

### Acknowledgements
I received inspiration for this project from [Gousto](https://www.gousto.co.uk/cookbook )
 
