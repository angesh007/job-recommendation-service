import sqlite3

def get_connection():
    conn = sqlite3.connect('jobs.db')
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      name TEXT, 
                      skills TEXT, 
                      experience_level TEXT, 
                      preferences TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs 
                      (job_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      job_title TEXT, 
                      company TEXT, 
                      required_skills TEXT, 
                      location TEXT, 
                      job_type TEXT, 
                      experience_level TEXT)''')

    conn.commit()
    conn.close()

def add_user_profile(profile):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (name, skills, experience_level, preferences)
                      VALUES (?, ?, ?, ?)''', 
                   (profile['name'], 
                    ','.join(profile['skills']), 
                    profile['experience_level'], 
                    str(profile['preferences'])))
    conn.commit()
    conn.close()

def get_job_postings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    conn.close()
    
    job_postings = []
    for row in rows:
        job_postings.append({
            'job_id': row[0],
            'job_title': row[1],
            'company': row[2],
            'required_skills': row[3].split(','),
            'location': row[4],
            'job_type': row[5],
            'experience_level': row[6]
        })
    return job_postings
