## Project Name

### Admin panel to manage companies

## Description
Basically, project to manage companies and their employees. Mini-CRM.
1. Basic Auth: ability to log in as administrator
2. Use database seeds to create first user with email admin@admin.com and password “password”
3. CRUD functionality (Create / Read / Update / Delete) for two menu items: Companies and
   Employees.
4.  Companies DB table consists of these fields: Name (required), email, logo (minimum 100×100),
  website
5. Employees DB table consists of these fields: First name (required), last name (required),
   Company (foreign key to Companies), email, phone
6. Use database migrations to create those schemas above
7. Store companies logos in storage/app/public folder and make them accessible from public


Basically, that’s it. With this simple exercise junior developer shows the skills in basic django things:
1. MVC
2. Auth
3. CRUD and Resource Controllers
4. Eloquent and Relationships
5. Database migrations and seeds
6. Form Validation and Requests
7. File management
8. Basic Bootstrap front-end
9. Pagination

## Installation
### To use the repository:
1. Clone the repository to a specified directory in your local machine.
2. Make sure python is installed in your local machine.
3. Use any of your favourite ide to view the code or make modifications to it.
4. Create a python environment wiith conda create --name myenv python=3.6
5. Install the requirements.txt with python -m pip install -r requirements.txt
6. Create a django project with django-admin startproject crm
7. Chabnge the directory to crm then run django-admin startapp api
8. Confirm everything is okay with python manage.py runserver
9. Run migrations with python manage.py makemigrations api then python manage.py makemigrations api then python manage.py migrate

### Live Link
The project is hosted on this link <https://tetcrm.herokuapp.com/> .The username credential is admin@gmail.com and password is Test123!4

## Contributing
This repository is owned by <https://github.com/EstherWaweru> . To contribute to this project raise an issue .
