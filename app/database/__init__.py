import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase:
    def create_database(self):
        # creds file should be downloaded from https://console.firebase.google.com/
        print("entered to firebase")
        cred = credentials.Certificate("room.json")
        firebase_admin.initialize_app(cred)
        self.database = firestore.client()

        
firebase = Firebase()