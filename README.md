# Flask API REST Template
Rest API template developed in Python with the Flask framework. The template covers user management, jwt tokens for authentication, and assign permissions for each user with Flask Principal. In the local environment, it uses docker to create an environment made up of several services such as api (flask), database (postgresql), swagger (swagger-ui), reverse-proxy (nginx), cron to perform database backups automatically.

## Index
- [Technology](#technology)
- [Requirements](#requirements)
- [Environments](#environments)
    - [Develop](#develop)
    - [Testing](#testing)
    - [Local](#local)
    - [Production](#production)
- [Backups](#backups)
- [Flask Commands](#flask-commands)
   - [Flask-cli](#flask-cli)
- [Database commands](#bbdd-commands)
   - [Flask-migrate](#flask-migrate)
- [Swagger](#swagger)
- [Reference](#reference)
- [Contribution](#contribution)

## Technology
- **Operating System:** Ubuntu 20.04
- **Web Framework:** Flask
- **ORM:** Flask-sqlalchemy
- **Swagger:** Swagger-UI
- **Authentication:** JSON Web Token
- **Permission:** Flask Principal
- **Serialization, Deserialization and Validation:** Marshmallow
- **Migration Database:** Flask-migrate
- **Authentication:** Flask-jwt-extended
- **Environment manager:** Anaconda/Miniconda
- **Containerization:** Docker, docker-compose
- **Database:** PostgreSQL 
- **Python WSGI HTTP Server:** Gunicorn
- **Proxy:** Nginx
- **Tests:** Unittest
- **Deployment platform:** AWS
- **CI/CD:** Github Actions

## Requirements
- [Python 3.9](https://www.python.org/downloads/)
- [Anaconda/Miniconda](https://www.hostinger.com/tutorials/how-to-install-anaconda-on-ubuntu/)
- [Docker 20.10.17](https://docs.docker.com/engine/install/ubuntu/)
- [Docker-Compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04)
- [Github](https://github.com)

## Environments
### Develop
Development environment that uses PostgreSQL in local and uses the server flask in debug mode.
1. Create environment and install packages:
    ```shell
    conda create -n backend python=3.9
    ```
    ```shell
    conda activate backend
    ```
    ```shell
    pip install -r requirements.txt
    ```
2. Create PosgresSQL on Ubuntu 20.04 
    Install PosgresSQL
    ```shell
    sudo apt-get install postgresql-12
    ```

    Go in PosgresSQL
    ```shell
    sudo -u postgres psql
    ```

    Create user and password
    ```shell
    CREATE USER db_user WITH PASSWORD 'db_password';
    ```
    
    Create Database dev
    ```shell
    CREATE DATABASE db_dev;
    ```

    Add permission User to Database
    ```shell
    GRANT ALL PRIVILEGES ON DATABASE db_dev TO db_user;
    ```

2. Create or update **.env** file and enter the environment variables of the environment.
3. Run:
    Create Database
    ```shell
    flask create-db
    ```

    Create User Admin
    ```shell
    flask create-user-admin
    ```

    Run a development server
    ```shell
    flask run
    ```

### Testing
Testing environment that uses PostgreSQL as database (db_test) and performs unit tests, integration tests and API tests.
1. Create environment and install packages:
    ```shell
    conda create -n backend python=3.9
    ```
    ```shell
    conda activate backend
    ```
    ```shell
    pip install -r requirements.txt
    ```
2. Create PosgresSQL on Ubuntu 20.04 
    Install PosgresSQL
    ```shell
    sudo apt-get install postgresql-12
    ```

    Go in PosgresSQL
    ```shell
    sudo -u postgres psql
    ```

    Create user and password
    ```shell
    CREATE USER db_user WITH PASSWORD 'db_password';
    ```
    
    Create Database test
    ```shell
    CREATE DATABASE db_test;
    ```

    Add permission User to Database
    ```shell
    GRANT ALL PRIVILEGES ON DATABASE db_test TO db_user;
    ```
2. Create or update **.env** file and enter the environment variables of the environment.
3. Init database:
    Create Database
    ```shell
    flask create-db
    ```

    Create User Admin
    ```shell
    flask create-user-admin
    ```

4. Run all the tests:
    ```shell
    pipenv run tests
    ```

5. Run unit tests:
    ```shell
    pipenv run tests_unit
    ```

6. Run integration tests:
    ```shell
    pipenv run tests_integration
    ```

7. Run API tests:
    ```shell
    pipenv run tests_api
    ```

8. Run coverage:
    ```shell
    pipenv run coverage
    ```

9. Run coverage report:
    ```shell
    pipenv run coverage_report
    ```

### Local
Containerized services separately with PostgreSQL databases (db), API (api) and Nginx reverse proxy (nginx) with Docker and docker-compose.

1. Create **.env.api.local**, **.env.db.local** and **.env.cron.local** files and enter environment variables for
    each service. In the local environment there are 4 services (api, db, nginx, cron). For example:
    1. **.env.api.local**:
       ```shell
       # APP configuration
       APP_NAME=[Name APP] # For example Flask API Rest Template
       APP_ENV=local
      
       # Flask configuration
       API_ENTRYPOINT=app:app
       APP_SETTINGS_MODULE=config.LocalConfig
       APP_TEST_SETTINGS_MODULE=config.TestingConfig
      
       # API service configuration
       API_HOST=<api_host> # For example 0.0.0.0
       API_PORT=<port_api> # For example 5000
      
       # Database service configuration
       DB_HOST=<name_container_bbdd> # For example db (name service in docker-compose)
       DB_PORT=<port_container_bbdd> # For example 5432 (port service in docker-compose)
       DATABASE=postgres
       DATABASE_TEST_URL=<url database test> # For example postgresql+psycopg2://db_user:db_password@db:5432/db_test
       DATABASE_URL=<url database> # For example postgresql+psycopg2://db_user:db_password@db:5432/db_dev
       ```
    2. **.env.db.local**:
       ```shell
       POSTGRES_USER=<name_user> # For example db_user
      
       POSTGRES_PASSWORD=<password> # For example db_password

       POSTGRES_DB=<name_DB> # For example db_dev
       ```
    3. **.env.cron.local**:
       ```shell
       # Service configuration DB backups

       # User to access the database server, example root
       BBDD_USER=<name_user> # For example root
        
       # Password to access the postgresql database
       PGPASSWORD=<password> # For example password
        
       # Host name (or IP address) of the PostgreSQL server, example localhost
       DB_HOST=<host> # For example db (name service in docker-compose)
        
       # PostgreSQL server port, example 5432
       BBDD_PORT=<port> # For example 5432 (port service in docker-compose)
        
       # Type of database
       DATABASE=<database_type> # For example postgres
        
       # List of DBNAMES for Daily/Weekly Backup e.g. "DB1DB2DB3"
       BACKUPS_DBNAMES=<tables> # For example all
        
       # Backup directory location e.g. /backups
       BACKUPS_BACKUPDIR=<backups_dir> # For example /var/backups/postgres
        
       # LOG directory location
       BACKUPS_LOGDIR=<dir_logs> # For example /var/log
        
       # List of DBNAMES to EXLUCDE if DBNAMES are set to all (must be in " quotes)
       BACKUPS_DBEXCLUDE=<tables> # For example db_test root postgres template0 template1
        
       # Include CREATE DATABASE in backup?
       BACKUPS_CREATE_DATABASE=<yes_or_no> # For example yes
        
       # Separate backup directory and file for each DB? (yes or no)
       BACKUPS_SEPDIR=<yes_or_no> # For example yes
        
       # Which day do you want weekly backups? (1 to 7 where 1 is Monday)
       BACKUPS_DOWEEKLY=<day_week> # For example 7
        
       # Which day do you want monthly backups? (1 to 28)
       BACKUPS_DOMONTHLY=<day_month> # For example 1
        
       # Choose Compression type. (gzip or bzip2)
       BACKUPS_COMP=<compression_type> # For example bzip2
        
       # Command to run before backups (uncomment to use)
       #BACKUPS_PREBACKUP=<command> # For example /etc/pgsql-backup-pre
        
       # Command run after backups (uncomment to use)
       #BACKUPS_POSTBACKUP=<command> # For example sh /home/backups/scripts/ftp_pgsql
       ```
2. Run:
    1. Build and run services:
       ```shell
       docker-compose up --build
       ```
    2. Stop services:
       ```shell
       docker-compose stop
       ```
    3. Delete services:
       ```shell
       docker compose down
       ```
    4. Remove services (removing volumes):
       ```shell
       docker-compose down -v
       ```
    4. Remove services (removing volumes and images):
       ```shell
       docker-compose down -v --rmi all
       ```
    5. View services:
       ```shell
       docker-compose ps
       ```
**NOTE:** The Rest API defaults to host *localhost* and port *8080*.

### Production
Apply CI/CD with Github Actions to automatically deployed to AWS platform use EC2, RDS PostgresSQL.

1. Create file **.env.pro** and enter the environment variables needed for production. For example:
    1. **.env.pro**:
       ```shell
       # APP configuration
       APP_NAME=Flask API Rest Template
       APP_ENV=production
      
       # Flask configuration
       API_ENTRYPOINT=app:app
       APP_SETTINGS_MODULE=config.ProductionConfig
      
       # API service configuration
       API_HOST=<api_host> # For example 0.0.0.0
      
       # Database service configuration
       DATABASE_URL=<url_database> # For example sqlite:///production.db
      
       # Deploy platform
       PLATFORM_DEPLOY=AWS
       ```
2. Create *Secrets* on Github:
    1. **AWS_ACCESS_KEY_ID**: access token
    2. **AWS_SECRET_ACCESS_KEY**: secret access
    3. **AWS_DEFAULT_REGION**: region

## Backups
In the local environment there is a service called `cron` and it is in charge of executing a script that performs a backup
from the database, in this case from postgresql. The script is run daily by cron and makes a copy
daily, weekly and monthly.

- `Daily` backups are rotated weekly.
- `weekly` backups are run by default on Saturday morning when cron.daily scripts are executed.
It can be changed with the `DOWEEKLY` setting. Weekly backups are rotated on a 5-week cycle.
- `Monthly` backups run on the 1st of every month. It can be changed with the `DOMONTHLY` setting.
   Monthly backups are NOT automatically rotated.

**Note:** It may be a good idea to copy the monthly backups offline or to another server.

## Flask Commands
### Flask-cli
- Create all tables in the database:
    ```
    flask create_db
    ```

- Delete all tables in the database:
    ```sh
    flask drop_db
    ```

- Create admin user for the Rest API:
    ```sh
    flask create-user-admin
    ```
    
- Database reset:
    ```sh
    flask reset-db
    ```
    
- Run tests without coverage:
    ```sh
    flask reset-db
    ```
    
- Run tests with coverage without report in html:
    ```sh
    flask cov
    ```
    
- Run tests with coverage with report in html:
    ```sh
    flask cov-html
    ```
     
## Database commands
### Flask-migrate
- Create a migration repository:
    ```sh
    flask db init
    ```

- Generate a migration version:
    ```sh
    flask db migrate -m "Init"
    ```
    
- Apply migration to the Database:
    ```sh
    flask db upgrade
    ```

## Swagger
```
http://localhost:port/swagger-ui
```
## Reference
- [Udemy - REST APIs with Flask and Python in 2023](https://www.udemy.com/course/rest-api-flask-and-python/)
- [Github - Flask API REST Template](https://github.com/igp7/flask-rest-api-template)

## Contribution
Feel free to make any suggestions or improvements to the project.