import firebase_admin
from firebase_admin import credentials, firestore
from catalogue.core import config

_db = None

def get_db():
    global _db
    if _db:
        return _db
    if not firebase_admin._apps:
        if config.GOOGLE_APPLICATION_CREDENTIALS:
            cred = credentials.Certificate(config.GOOGLE_APPLICATION_CREDENTIALS)
        else:
            cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {"projectId": config.FIREBASE_PROJECT_ID})
    _db = firestore.client()
    return _db
