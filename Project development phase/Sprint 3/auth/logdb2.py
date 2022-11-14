'''
These file load credentials for database  db2 and make connection db2
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('./auth/serviceAccountKey.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
