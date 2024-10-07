def recommend_jobs(profile, job_postings):
    matched_jobs = []
    
    for job in job_postings:
        # Match skills
        if not set(profile['skills']).intersection(set(job['required_skills'])):
            continue
        # Match experience level
        if profile['experience_level'] != job['experience_level']:
            continue
        # Match job type and location preferences
        if job['job_type'] != profile['preferences']['job_type']:
            continue
        if job['location'] not in profile['preferences']['locations']:
            continue
        
        matched_jobs.append(job)
    
    return matched_jobs
