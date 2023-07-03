# Flask API REST Template
Rest API template developed in Python with the Flask framework. The template covers user management, jwt tokens for authentication, and assign permissions for each user with Flask Principal. In the local environment, it uses docker to create an environment made up of several services such as api (flask), database (postgresql), swagger (swagger-ui), reverse-proxy (nginx), cron to perform database backups automatically.

## Technology
- **Web Framework:** Flask
- **ORM:** Flask-sqlalchemy
- **Swagger:** Swagger-UI
- **Authentication:** JSON Web Token
- **Permission:** Flask Principal
- **Serialization, Deserialization and Validation:** Marshmallow
- **Migration Database:** Flask-migrate
- **Authentication:** Flask-jwt-extended
- **Environment manager:** Pipenv
- **Containerization:** Docker docker-compose
- **Database:** PostgreSQL 
- **Python WSGI HTTP Server:** Gunicorn
- **Proxy:** Nginx

To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

## Set up environment
```
conda create -n backend python=3.10
```
```   
conda activate backend
```
```
pip install -r requirements.txt
```
## Start server
```
cd app
```
```
python manage.py
```
## Set up database - postgresql (Manual) - Config path in config.py
### Initialize the database with Flask-Migrate
Activate your virtual environment and run this command:
```
flask db init
```
### Generate the first migration to set up the database or update whenever change somethings
```
flask db migrate
```
```
flask db upgrade
```
### Add initial data
```
python init_data.py
```
## API Document
```
http://127.0.0.1:3000/swagger-ui
```


## Create PosgresSQL on Ubuntu 20.04 (Local)
### Step 1: Install PosgresSQL
```
sudo apt-get install postgresql-12
```
### Step 2: Go in PosgresSQL
```
sudo -u postgres psql
```
### Step 3: Create user and password
```
CREATE USER myuser WITH PASSWORD 'mypassword';
```
### Step 4: Create Database
```
CREATE DATABASE mydatabase;
```
### Step 5: Add permission User to Database
```
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
```