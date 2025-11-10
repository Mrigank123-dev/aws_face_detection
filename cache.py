from flask import current_app
from database import db, Student, Face

# In-memory cache for face encodings
known_faces_cache = {
    'encodings': [],
    'student_ids': [],
    'names': []
}

def load_known_faces():
    """
    Loads all face encodings from the database into the global 'known_faces_cache'.
    This function needs the app context to query the database.
    """
    global known_faces_cache
    print("Reloading known faces cache...")
    
    # We use current_app.app_context() to ensure we can access the database
    with current_app.app_context():
        known_faces = db.session.query(
            Face.encoding, 
            Student.id, 
            Student.name
        ).join(Student, Face.student_id == Student.id).all()
        
        if known_faces:
            # Unzip the query results into separate lists
            encodings, student_ids, names = zip(*known_faces)
            known_faces_cache = {
                'encodings': list(encodings),
                'student_ids': list(student_ids),
                'names': list(names)
            }
        else:
            # Ensure cache is empty if database is empty
            known_faces_cache = {'encodings': [], 'student_ids': [], 'names': []}
            
        print(f"Cache reloaded. Total encodings: {len(known_faces_cache['encodings'])}")