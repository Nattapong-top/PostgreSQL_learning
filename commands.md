````md
# Docker Commands

## Start Container

```bash
docker compose up -d
````

## Stop Container

```bash
docker compose down
```

## Check Running Containers

```bash
docker ps
```

---

# PostgreSQL Commands

## Enter PostgreSQL

```bash
docker exec -it postgres-db psql -U postgres -d hospital_db
```

## Run SQL File

```bash
docker exec -i postgres-db psql -U postgres -d hospital_db < sql/001_create_patients.sql
```

---

# psql Commands

## Show Tables

```sql
\dt
```

## Show Databases

```sql
\l
```

## Connect Database

```sql
\c hospital_db
```

## Exit psql

```sql
\q
```

```
```
