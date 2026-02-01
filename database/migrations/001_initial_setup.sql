-- Migration: 001_initial_setup
-- Description: Initial database setup for VNStock Analytics
-- Date: 2024-02-01

BEGIN;

-- Run the main schema file
\i '../schema.sql'

COMMIT;
