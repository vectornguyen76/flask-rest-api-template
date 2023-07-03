#!/bin/sh

echo "# do daily/weekly/monthly maintenance" > /etc/crontabs/root
echo "# min	hour	day	month	weekday	command" >> /etc/crontabs/root
echo "*/15	*	*	*	*	run-parts /etc/periodic/15min" >> /etc/crontabs/root
echo "0	*	*	*	*	run-parts /etc/periodic/hourly" >> /etc/crontabs/root
echo "0	2	*	*	*	run-parts /etc/periodic/daily" >> /etc/crontabs/root
echo "0	3	*	*	6	run-parts /etc/periodic/weekly" >> /etc/crontabs/root
echo "0	5	1	*	*	run-parts /etc/periodic/monthly" >> /etc/crontabs/root

crontab -l

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $BBDD_HOST $BBDD_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# start cron
/usr/sbin/crond -f -l 0