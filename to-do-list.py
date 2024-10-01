import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("to-do-list.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

results = db.collection('project').document('chores').get()

data = results.to_dict()
print(data)