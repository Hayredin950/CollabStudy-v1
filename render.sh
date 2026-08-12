#!/usr/bin/env bash
# Render free-tier startup script.
# preDeployCommand is unavailable on free services, so we run migrations here
# on every boot (they are idempotent) before starting gunicorn.
set -e

python manage.py migrate --noinput

exec gunicorn studybudd.wsgi:application \
  --workers 2 \
  --worker-class gthread \
  --threads 4 \
  --timeout 120 \
  --bind 0.0.0.0:${PORT}
