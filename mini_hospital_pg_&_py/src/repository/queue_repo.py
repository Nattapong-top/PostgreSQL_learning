from uuid import UUID

from datetime import datetime


import psycopg2

from domain.patient import PatientID
from domain.queue import Queue, QueueStatus, QueueID
from repository.base import QueueABC


class QueueRepo(QueueABC):

    AUTO_CREATE_QUEUE_TABLE = """
    CREATE TABLE IF NOT EXISTS queue (
        id UUID PRIMARY KEY,
        patient_id UUID,
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

    UPDATE_STATUS = """
    UPDATE queue SET status = %s WHERE id = %s
    """

    SELECT_QUEUE_ID = """
    SELECT id, patient_id, queue_number, status, created_at FROM queue WHERE id = %s
    """

    SELECT_ALL_QUEUE = """
    SELECT * FROM queue
    """

    def __init__(self, db_config: dict) -> None:
        self.db_config = db_config
        self.auto_create_queue_table()

    def auto_create_queue_table(self):
        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(self.AUTO_CREATE_QUEUE_TABLE)
                    conn.commit()
                    print("created queue table successfully")

        except psycopg2.Error as e:
            conn.rollback()
            print("failed to create queue table")
            print(f"error: {e}")

    #
    def add_queue(self, queue: Queue) -> None:
        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        self.INSERT_INTO_QUEUE,
                        (
                            str(queue.id.id),
                            str(queue.patient_id.id),
                            queue.queue_number,
                            queue.status.value,
                            queue.created_at.isoformat(),
                        ),
                    )
                conn.commit()
                print(f"added queue {queue.queue_number} successfully")
        except psycopg2.Error as e:
            conn.rollback()
            print(f"failed to add queue {queue}")
            print(f"error: {e}")

    def update_status(self, queue: Queue, status: QueueStatus) -> None:

        data = (
            status.value,
            str(queue.id.id),
        )

        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(self.UPDATE_STATUS, data)
                    conn.commit()
                    print(f"updated queue {queue.queue_number} successfully")
        except psycopg2.Error as e:
            conn.rollback()
            print(f"failed to update queue {queue}")
            print(f"error: {e}")

    @staticmethod
    def _map_to_queue_entity(
        row_queue: tuple[UUID, UUID, int, QueueStatus, datetime],
    ) -> Queue:
        q_id, p_id, q_number, status, created_at = row_queue

        queue_entity = Queue(
            id=QueueID(id=q_id),
            patient_id=PatientID(id=p_id),
            queue_number=q_number,
            status=QueueStatus(status),
            created_at=created_at,
        )
        return queue_entity

    def find_by_queue_id(self, queue_id: QueueID) -> Queue | None:
        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(self.SELECT_QUEUE_ID, (str(queue_id.id),))
                    row_queue = cur.fetchone()

                    if not row_queue:
                        return None

                    queue_entity = self._map_to_queue_entity(row_queue)
                    print(f"found queue: {queue_entity}")
                    return queue_entity

        except psycopg2.Error as e:
            conn.rollback()
            print(f"failed to find queue {queue_id}")
            print(f"error: {e}")
            return None

    def find_all_queue(self) -> list[Queue] | None:
        try:
            queues = []
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(self.SELECT_ALL_QUEUE)
                    for row_queue in cur.fetchall():
                        queue_entity = self._map_to_queue_entity(row_queue)
                        queues.append(queue_entity)
            return queues
        except psycopg2.Error as e:
            conn.rollback()
            print("not find all queues")
            print(f"error: {e}")
            return None
