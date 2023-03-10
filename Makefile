mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	./manage.py admin_user

data:
	./manage.py loaddata currency.json
	./manage.py loaddata category.json
	./manage.py loaddata countries.json

unmig:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

remig:
	./manage.py remig
	make admin --no-print-directory -s
	make data --no-print-directory -s
	make fake --no-print-directory -s

fake:
	./manage.py fake_models -u 2 -sh 4 -p_c 10 -p 100 -o 100 -d 4

test:
	pytest && open coverage/index.html

create_database_function:
	./manage.py create_database_func