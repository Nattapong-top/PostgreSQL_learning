#!/bin/bash
docker exec -i postgres-db psql -U postgres -d hospital_db < sql/000_reset.sql
docker exec -i postgres-db psql -U postgres -d hospital_db < sql/001_create_patients.sql
docker exec -i postgres-db psql -U postgres -d hospital_db < sql/002_insert_patients.sql
docker exec -i postgres-db psql -U postgres -d hospital_db < sql/003_create_staff.sql
docker exec -i postgres-db psql -U postgres -d hospital_db < sql/004_create_queues.sql
docker exec -i postgres-db psql -U postgres -d hospital_db < sql/005_insert_into_patients.sql