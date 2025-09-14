-- 00_create_tables_and_sample_data.sql
-- Replace project_id and dataset with your own GCP project and dataset.
-- Run this in BigQuery console or via client libraries.

-- === CONFIG: replace these ===
-- PROJECT: your GCP project id
-- DATASET: ai_learning_buddy

-- Example: CREATE SCHEMA IF NOT EXISTS `your-project-id.ai_learning_buddy`;

CREATE OR REPLACE TABLE `your-project-id.ai_learning_buddy.lesson_content` (
  id STRING,
  text STRING
);

CREATE OR REPLACE TABLE `your-project-id.ai_learning_buddy.simple_content` (
  id STRING,
  text STRING
);

-- Small sample seed rows for demo / offline evaluation
INSERT INTO `your-project-id.ai_learning_buddy.lesson_content` (id, text)
VALUES
  ("lc_001", "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods from carbon dioxide and water."),
  ("lc_002", "Mitosis is a type of cell division that results in two daughter cells each having the same number and kind of chromosomes as the parent nucleus.");

INSERT INTO `your-project-id.ai_learning_buddy.simple_content` (id, text)
VALUES
  ("sc_001", "Plants make food using sunlight, air, and water. This process is called photosynthesis."),
  ("sc_002", "Mitosis is when a cell splits to make two identical cells. It helps organisms grow and replace damaged cells.");
