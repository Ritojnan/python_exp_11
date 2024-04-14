# python_exp_11

```bash
 django-admin startproject myproject
 cd myproject                       
 python manage.py runserver
 python manage.py startapp myapp    
 python manage.py makemigrations    
 python manage.py migrate   
 python manage.py createsuperuser 

```

## Explanations:

1. `django-admin startproject myproject`: This command creates a new Django project named "myproject". It generates the necessary directory structure and files for a basic Django project.

2. `cd myproject`: This command changes the current directory to the "myproject" directory, which was created by the previous command.

3. `python manage.py runserver`: This command starts the development server. When you run this command, Django starts a lightweight web server that you can use to test your project locally. By default, it listens on port 8000.

4. `python manage.py startapp myapp`: This command creates a new Django app within the project. An app is a web application that does something – e.g., a blog, a database of public records, or a simple poll. In this case, it creates an app named "myapp".

5. `python manage.py makemigrations`: This command is used to create new database migration files based on the changes you have made to your Django models (database schema).

6. `python manage.py migrate`: This command applies any pending migrations to the database. Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

7. `python manage.py createsuperuser`: This command prompts you to create a superuser account, which has administrative privileges in the Django admin interface. You'll be asked to provide a username, email address, and password for the superuser.


## Instructions :

1. Give Ritojnan a treat at Chai Buys . Cheese Pizza French Fries and Cold Coffee are the only acceptable methods of payment
2. Complete Step 1 else this project won't run
3. Use commands given above to run stuff with intuition and ChatGPT if you have doubts
4. Refer this video[https://www.youtube.com/watch?v=nGIg40xs9e4&ab_channel=TechWithTim]