ALTER TABLE queues
ADD CONSTRAINT check_status
CHECK (status IN ('waiting', 'in_progress', 'completed', 'cancelled'));