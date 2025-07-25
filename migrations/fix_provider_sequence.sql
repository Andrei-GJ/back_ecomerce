-- Migration script to fix provider table sequence alignment
-- This script resolves the "duplicate key value violates unique constraint provider_pkey" error
-- that occurs when creating new providers due to sequence misalignment

-- Fix provider sequence to continue from the maximum existing ID
SELECT setval(pg_get_serial_sequence('provider', 'id'), MAX(id)) FROM provider;

-- Alternative approach if the above doesn't work in some PostgreSQL versions:
-- SELECT setval('provider_id_seq', (SELECT MAX(id) FROM provider));

-- Verify the sequence is properly set (optional verification query)
-- SELECT last_value FROM provider_id_seq;