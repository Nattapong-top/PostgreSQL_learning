BEGIN;
    UPDATE queues SET status = 'cancelled'
    WHERE patient_id = 2;
    UPDATE patients SET  last_name = 'Cancelled' WHERE id = 2;
COMMIT;


BEGIN;
    UPDATE queues SET status = NULL
    WHERE patient_id = 2;
    UPDATE patients SET  last_name = 'Cancelled' WHERE id = 2;
ROLLBACK;
