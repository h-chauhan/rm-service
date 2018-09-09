import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from .settings import BASE_DIR
import os

# Use a service account
cred = credentials.Certificate(os.path.join(BASE_DIR, 'service.json'))
firebase_admin.initialize_app(cred)

db = firestore.client()