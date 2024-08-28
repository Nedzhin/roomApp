from database import firebase
from models.constants import collection

def delete_user(id: str):
    return firebase.database.collection(u'{collection}'.format(collection=collection)).document(u'{id}'.format(id=id)).delete()