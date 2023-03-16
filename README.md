# Template Flask RestAPI
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