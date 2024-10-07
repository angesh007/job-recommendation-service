from flask import Flask, request, jsonify
from recommendation.logic import recommend_jobs
from database.db_setup import get_job_postings, add_user_profile

app = Flask(__name__)

@app.route('/profile', methods=['POST'])
def add_profile():
    try:
        profile = request.json
        add_user_profile(profile)
        return jsonify({'message': 'Profile added successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    try:
        profile = request.json
        job_postings = get_job_postings()
        recommendations = recommend_jobs(profile, job_postings)
        return jsonify(recommendations), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
