#!/bin/sh
python manage.py migrate
echo "Starting backend at http://127.0.0.1:8000"
exec "$@"
