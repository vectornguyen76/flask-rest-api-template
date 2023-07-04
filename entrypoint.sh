#!/bin/sh

echo "Database:" $DATABASE

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nmap -p $BBDD_PORT --open -oG - $BBDD_HOST ; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Enviroment:" $APP_ENV

if [ "$APP_ENV" = "local" ]; then
    echo "Start create database"
    flask create-db
    echo "Done create database"

    echo "Start check user-admin"
    flask create-user-admin
    echo "Done init user-admin"

    echo "Run app with gunicorn server..."
    gunicorn --bind $API_HOST:$API_PORT $API_ENTRYPOINT --timeout 10 --workers 4;
fi