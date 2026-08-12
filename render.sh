#!/usr/bin/env bash
# Render free-tier startup script.
# preDeployCommand is unavailable on free services, so we run migrations here
# on every boot (they are idempotent) before starting gunicorn.
set -e

# Render may boot the web service before the managed Postgres is fully
# reachable on the very first deploy. Wait (bounded) for the database so a
# transient DNS/connection race doesn't kill the deploy.
python - <<'PY'
import os
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybudd.settings')
import django

django.setup()
from django.db import connection
from django.db.utils import OperationalError

for attempt in range(30):
    try:
        connection.ensure_connection()
        print("Database connection established.")
        break
    except OperationalError as exc:
        print(f"Database not ready (attempt {attempt + 1}/30): {exc}")
        time.sleep(10)
else:
    raise SystemExit(
        "Database did not become reachable within the wait window. "
        "Check that the Postgres instance is Available and that the web "
        "service's DATABASE_URL uses the correct internal/external URL "
        "for its region."
    )
PY

python manage.py migrate --noinput

exec gunicorn studybudd.wsgi:application \
  --workers 2 \
  --worker-class gthread \
  --threads 4 \
  --timeout 120 \
  --bind 0.0.0.0:${PORT}
