from database import firebase
from fastapi.exceptions import HTTPException
from models.constants import collection
from typing import Optional

def get_user(user_tid: str):
    db = firebase.database
    doc_ref = db.collection(u'{collection}'.format(collection=collection)).document(u'{user_tid}'.format(user_tid=user_tid))
    print("entered to the getting data from firebase")
    doc = doc_ref.get()
    doc_data = doc.to_dict()
    print(doc)
    if doc_data["purpose"] == "False":
        purpose_ref = doc_ref.collection('rent_purpose').get()
    else:
        purpose_ref = doc_ref.collection('travel_purpose').get()
        
    print("purposes:", purpose_ref)
    purposes = [pur.to_dict() for pur in purpose_ref]

    return {'anketa': doc_data , 'purpose': purposes}


def get_user_filter(status: Optional[str] = None, gender: Optional[str] = None, age: Optional[int] = None, city: Optional[str] = None, request_id: Optional[str] = None):
    db = firebase.database
    users_ref = db.collection("users")
    query = users_ref

    # Apply status filter if provided
    if status:
        query = query.where("status", "==", status)

    # Apply gender filter if provided
    if gender:
        query = query.where("gender", "==", gender)

    # Apply age filter if provided
    if age:
        query = query.where("gender", "==", 2024 - gender)

    if city:
        query = query.where("city", "==", city)
    # if min_age and max_age:
    #     query = query.where("age", ">=", min_age).where("age", "<=", max_age)
    # elif min_age:
    #     query = query.where("age", ">=", min_age)
    # elif max_age:
    #     query = query.where("age", "<=", max_age)

    # Fetch and return matching profiles
    results = query.stream()
    profiles = [doc.to_dict() for doc in results]
    
    
    if not profiles:
        raise HTTPException(status_code=404, detail="No matching profiles found")
    
    
    new_enter = users_ref.document(request_id)
    new_enter.collection("f_profiles").document(request_id).set({
        "found_profiles": profiles    }
        )
    print("request id bar eken", request_id)

    return {"profiles": profiles}

def get_filtered_profiles(request_id):
    db = firebase.database
    doc_ref = db.collection(u'{collection}'.format(collection=collection)).document(u'{user_tid}'.format(user_tid=request_id))
    print("entered to the getting data from firebase")
    #doc = doc_ref.get()
    #doc_data = doc.to_dict()
    #print(doc

    filtered_profiles = doc_ref.collection("f_profiles").document(request_id).get()
    final_profiles = filtered_profiles.to_dict()#[pur.to_dict() for pur in filtered_profiles] 
    return { 'filtered_profiles': final_profiles}