from database import firebase
from fastapi.exceptions import HTTPException
from models.constants import collection

def get_user(id: str):
    db = firebase.database
    doc_ref = db.collection(u'{collection}'.format(collection=collection)).document(u'{id}'.format(id=id))
    doc = doc_ref.get()
    return doc.to_dict()