DB=docker exec -i mini_hospital_db psql -U postgres -d mini_hospital_db

up:
	docker compose up -d

down:
	docker compose down

run:
	$(DB) < $(f)

psql:
	decker exec -it mini_hospital_db psql -U postgres -d mini_hospital_db

reset:
	$(DB) -c "DROP TABLE IF EXISTS queues, staff, patients CASCADE;"

seed:

py_run:
	python src/main.py

check:
	ruff check .
	black --check .

fix:
	ruff check . --fix
	black .