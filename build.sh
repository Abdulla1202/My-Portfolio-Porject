#!/usr/bin/env bash
# Vercel build script
set -o errexit

pip install -r requirements.txt

cd portfolio
python manage.py collectstatic --no-input
