# Django/Nuxt based Recipe Application

## Prerequisites

Python 3.5 or higher

## Deployment steps

A separate instance of the Django backend and the Nuxt frontend are required to run concurrently. This can be accomplished through the use of screen sessions, tmux, or even separate terminal windows/panes. 
### Google API

To allow for authenticating using a Google account, it is necessary to first setup a Google API project. Instructions on how to set up a project can be found in the following dev.to tutorial written by Muhd Rahiman

[Django Google Authentication using django-allauth](https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8)

Note your ClientID and Secret key once the project is created

### Backend

Install backend package dependencies
```
# Run from base directory of repostiory
pip install pipenv
pipenv shell
pipenv sync
```

Generate secret key for application
```
dsk=$(python -c "import secrets; print(secrets.token_urlsafe())")
echo DJANGO_SECRET_KEY=$dsk > backend/.env
```

Populate database and create a super user
```
cd backend
python manage.py migrate
python manage.py createsuperuser
```

Run the backend server
```
python manage.py runserver
```

Add Social Account for Google in Django admin interface
* Browse to http://localhost:8000/admin # port may vary depending on config or if multiple django instances are running
* Log in with super user credentials
* Browse to 'Social applications' and click '+ Add'.
    * Provider: Google
    * Name: Google Auth
    * Client Id: Id acquired from Google API Project
    * Secret key: Key acquired from Google API Project
    * Chosen Sites: example.com
* Save the new application

### Frontend

Installing package dependencies
```
pipenv shell
cd frontend
npm install
```

Run the frontend server
```
npm run dev
```



