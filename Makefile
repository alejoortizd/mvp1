up:
	docker compose up
down:
	docker compose down
build:
	docker compose build
makemigrations:
	docker compose run --rm django python manage.py makemigrations
migrate:
	docker compose run --rm django python manage.py migrate
shell:
	docker compose run --rm django python manage.py shell_plus
superuser:
	docker compose run --rm django python manage.py createsuperuser
tailinstall:
	docker compose run --rm django python manage.py tailwind install
tailbuild:
	docker compose run --rm django python manage.py tailwind build
taildev:
	docker compose run --rm django python manage.py tailwind start
