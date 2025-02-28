# Job Recommendation Service

This project is a RESTful API service that recommends job postings based on user profiles, skills, experience levels, and preferences.

## Features
- Accept user profile data via `/profile` endpoint.
- Return job recommendations based on matching logic via `/recommendations` endpoint.
- Store user profiles and job postings in an SQLite database.

## Setup Instructions
### Prerequisites
- Python 3.7+
- `pip` for installing dependencies

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the application: `python app.py`.

## API Endpoints
- `/profile`: Accepts user profile data (POST).
- `/recommendations`: Returns recommended jobs based on user profile (POST).

## Matching Algorithm
- The recommendation logic is based on a rule-based system that matches skills, experience, and preferences with job postings.

## Assumptions & Challenges
- Assumed that the user profile contains complete data.
