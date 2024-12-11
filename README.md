
# Nutrimind

Nutrimind is a personalized web app designed with Django  to help users generating a meal plan and yoga exercises according to their psychological conditions


## Features

- Authentication: user can login register and logout securely
- Profile management: users can input their name,age,weight,and select psychological conditions.
- Personalized recommendations: meal plan and yoga exercise will be suggested based on their selected conditions
- Used Fetch API for handling form submission and saving profiles plans for future reference
- Users can save their profiles and revisit their personalized plans later


## Installation

Install my-project 

```bash
  Run in terminal: cd project5
  python manage.py runserver 
  open local host  http://127.0.0.1:8000

```
    
## Tech Stack

**Frontend:** HTML, CSS, JAVASCRIPT

**Backend:** DJANGO, PYTHON

**Database:** SQlite(Django database)



## Files and Directories

#### Project5  main  application directory

- nutrimind app
    ###### admins.py 	provide admin interface to manage models in the project
    ###### 	forms.py	contain a django form to manage user input
    ###### models.py	consist of 4 models  
        `Psychological condition: which user can select and it will be displayed on the admins interface along with user name`

        `the Abstract user model`
        `UserProfile which is linked to the user model that ensure each user has only one profile and stores personal information of user like age weight name etc `
        `Recommendation model links meal plan and a yoga exercise using a foreign key to a specific psychological condition`

- Urls.py	:Contains all url paths for application like login ,logout,register,profile input,meals recommendation, user saved data for future reference

- Views.py:Contains all view functions for base layout login-user page, logout, and register user. loguser serves as the home page and index page, which takes data from the user and renders the recommendation view. If the user saves their profile, they can revisit their saved information.
- Static consist of all static files including
```image```
```contains all the static images and icons```

```css```
```contain file for styling the whole website```

```js```
    ```It ensures that users can save their profiles efficiently using fetch api it collects profile data from frontend and send it to server without reloading the page and handles server response and errors```
- Project5: contains all the settings and main url files
- Templates holds all the html files



## Distinctivesness

 - Used multiple models
 - Personalized meal plans and yoga exercise recommendations  based on the users selected psychological condition shows a unique relation between user data and output.   
 - User can revisit and save their plans make it distinct from other one-time-use applications. 
 - Using django’s ORM manages data relationship (linking psychological condition with recommendation ) for saving retrieving and updating user’s data 
 - Used fetch API for form submission without page reload make a seamless interaction of frontend and backend
 - Completely responsive interface
 - Secure user authentication system 


## Demo
![image alt](https://github.com/am-ber098/sampleproject/blob/master/Screenshot%202024-12-11%20at%2019-14-34%20Social%20nutrimind.png?raw=true)
