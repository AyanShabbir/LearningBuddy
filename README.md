AI Learning Buddy – Adaptive Learning for Unprivileged Students

Project Overview

**AI Learning Buddy** is an AI-powered educational assistant designed to help students in unprivileged areas learn more effectively. It automatically generates questions, summaries, and adaptive learning paths based on lesson content, making learning more personalized and engaging.

The project is built as a complete end-to-end pipeline:

- **Lesson Content** → **Question Generation** → **Summaries** → **Adaptive Recommendations**

This project was developed for the [BigQuery AI Hackathon](https://www.kaggle.com/competitions/bigquery-ai-hackathon)

---

## Motivation

Students in unprivileged areas often lack access to structured learning resources. AI Learning Buddy provides:

- Automated **question generation** to test understanding  
- **Summaries at multiple levels** for adaptive learning  
- **Personalized learning paths** to ensure gradual progression  
- A pipeline that can scale to larger datasets for real-world applications

---

## Dataset

The dataset used in this project (`example_study_pack.csv`) contains:

| Column | Description |
|--------|-------------|
| `id` | Unique identifier for each lesson |
| `subject` | Lesson subject (Science, Math, Geography) |
| `level` | Difficulty level (Easy, Medium, Hard) |
| `content` | Text content of the lesson |

**Number of entries:** 21 lessons covering multiple subjects and difficulty levels.

---

## Project Structure


- **data/** – contains sample lesson content and final output CSVs.  
- **notebooks/** – step-by-step workflow with Markdown explanations.  
- **src/** – Python modules for question generation, summarization, and learning paths.  
- **requirements.txt** – Python dependencies.  

---

## Installation & Setup

1. **Clone the repository:**

git clone <your-repo-url>
cd Hybrid-AI-Learning


2. **Create a virtual environment:**

python -m venv venv
# Activate (Linux/Mac)
source venv/bin/activate
# Activate (Windows PowerShell)
venv\Scripts\Activate.ps1


3. **Install dependencies:**

pip install --upgrade pip
pip install -r requirements.txt


4. **Run notebooks in order:**

01_explore_data.ipynb – Explore dataset

02_generate_questions.ipynb – Generate MCQs, short-answer, and open-ended questions

03_generate_summaries.ipynb – Summarize lessons at 3 difficulty levels

04_learning_paths.ipynb – Generate adaptive learning recommendations



**How It Works**

Question Generation

Uses Hugging Face transformers pipeline to generate MCQs, short-answer, and open-ended questions.

Progress bars (tqdm) included for tracking multiple lessons.

Summarization

Generates simple, medium, and advanced summaries for each lesson.

Summaries help students grasp core concepts at their level.

Adaptive Learning Paths

Simulates student scores and recommends next lessons based on performance.

Ensures progressive learning and reinforcement.


**BigQuery AI Integration**

For hackathon authenticity, BigQuery AI SQL snippets were added in the notebooks, demonstrating how AI-generated questions could run on bqai.text-bison


