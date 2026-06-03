DB=docker exec -i postgres-db psql -U postgres -d hospital_db

up:
	docker compose up -d

down:
	docker compose disown

reset:
	$(DB) < sql/000_reset.sql

seed:
	$(DB) < sql/001_create_patients.sql
	$(DB) < sql/002_insert_patients.sql
	$(DB) < sql/003_create_staff.sql
	$(DB) < sql/004_create_queues.sql
	$(DB) < sql/005_insert_queues.sql

psql:
	docker exec -it postgres-db psql -U postgres -d hospital_db