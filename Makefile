SHELL=/bin/bash

lint:
	flake8 --max-complexity 10

test:
	pytest

check: lint test

format_code:
	black .

create_admin:
	python manage.py init_admin