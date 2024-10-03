import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("to-do-list.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

results = db.collection('project').get()
total = 0
for result in results:
    data = result.to_dict()
    print(f"{result.id} : {data['name']}")