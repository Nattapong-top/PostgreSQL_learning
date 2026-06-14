import psycopg2
from domain.queue import Queue


class QueueRepo:


    AUTO_CREATE_QUEUE_TABLE = """
    CREATE TABLE IF NOT EXISTS queue (
        id TEXT PRIMARY KEY,
        patient_id TEXT,
        queue_number INTEGER,
        status TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """
    #
    INSERT_INTO_QUEUE = """
    INSERT INTO queue (
    id, patient_id, queue_number, status, created_at)
    VALUES (%s, %s, %s, %s, %s)
    """
    #
    #



    def __init__(self, db_config: dict) -> None:
        self.db_config = db_config
        self.auto_create_queue_table()

    def auto_create_queue_table(self):
        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(self.AUTO_CREATE_QUEUE_TABLE)
                    conn.commit()
                    print('created queue table successfully')

        except psycopg2.Error as e:
            conn.rollback()
            print('failed to create queue table')
            print(f'error: {e}')
    #
    def add_queue(self, queue: Queue) -> None:
        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(self.INSERT_INTO_QUEUE,
                (
                        str(queue.id.id),
                        str(queue.patient_id.id),
                        queue.queue_number,
                        queue.status.value,
                        queue.created_at.isoformat(),
                    ),
                )
                conn.commit()
                print(f'added queue {queue.queue_number} successfully')
        except psycopg2.Error as e:
            conn.rollback()
            print(f'failed to add queue {queue}')
            print(f'error: {e}')
