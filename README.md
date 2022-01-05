# Django/Nuxt based Recipe Application

## Prerequisites

Python 3.5 or higher

## Deployment steps

A separate instance of the Django backend and the Nuxt frontend are required to run concurrently. This can be accomplished through the use of screen sessions, tmux, or even separate terminal windows/panes. 

### Backend

Install backend package dependencies
```
# Run from base directory of repostiory
pip install pipenv
pipenv shell
pipenv install
```

Generate secret key for application
```
python -c "import secrets; print(secrets.token_urlsafe())"
```

Create a `backend/.env` file and populate it with
```
DJANGO_SECRET_KEY=<Generated Secret Key>
```

Populate database and run backend
```
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runsever
```

### Frontend

Installing package dependencies
```
pipenv shell
pipenv install npm
cd frontend
npm install
```

```
npm run dev
```



