SHELL=/bin/bash

lint:
	flake8
	mypy --sqlite-cache .

test:
	pytest

check: lint test

format_code:
	black .

create_admin:
	python manage.py init_admin

base:
	python manage.py make_base