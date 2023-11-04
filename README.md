## INF601VA - Advanced Programming in Python
# Steven Burris
# 10-30-2023
# *Mini Project 4 SBurris*
# *Social App*

# *Description*
### With this app, admin can add a post that has title input, description input, image input, and set choices to vote on in each post
### Users can log in and see the admin posts and vote on the choices
## *PIP Install Instructions*
Please copy the following command in the terminal for all the packages needed to run the program:
```
pip install -r requirements.txt
```

## How to set up database
(this will create any SQL entries that need to go into the database)
```
python manage.py makemigrations socialapp
```
(this will show tables created)
```
python manage.py sqlmigrate socialapp 0001
```
(this will apply the migrations)
```
python manage.py migrate
```

## How to create the main admin user
(this will create the administrator login for your /admin side of your project)
```
python manage.py createsuperuser 
```


# Then start app
```
python manage.py runserver
``` 

# This is the link to go to the admin page to add, edit, and delete socialapp post items
Administration url : [Administration url](http://127.0.0.1:8000/admin)