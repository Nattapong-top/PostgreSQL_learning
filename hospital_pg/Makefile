DB=docker exec -i hospital_pg psql -U postgres -d hospital_pg

up:
	docker compose up -d

down:
	docker compose down

run:
	$(DB) < $(f)

psql:
	decker exec -it hospital_pg psql -U postgres -d hospital_pg

reset:
	$(DB) -c "DROP TABLE IF EXISTS queues, staff, patients CASCADE;"

seed:
	$(DB) < sql/001_create_table.sql