from database import firebase
from models.constants import collection

def create_user(id: str,username: str, usersurname: str, gender: str, birthday: str, city: str, education: str, job: str, info: str):
    print("entered to services")
    firebase.database.collection(u'{collection}'.format(collection=collection)).document(u'{id}'.format(id=id)).set({
        u'username': u'{username}'.format(username=username),
        u'usersurname': u'{usersurname}'.format(usersurname=usersurname),
        u'gender': u'{gender}'.format(gender=gender),
        u'birthday': u'{birthday}'.format(birthday=birthday),
        u'city': u'{city}'.format(city=city),
        u'education': u'{education}'.format(education=education),
        u'job': u'{job}'.format(job=job),
        u'info': u'{info}'.format(info=info),
    })
    
    return {
        'id': id,
        'username': '{username}'.format(username=username),
        'usersurname': u'{usersurname}'.format(usersurname=usersurname),
        'gender': '{gender}'.format(gender=gender),
        'birthday': '{birthday}'.format(birthday=birthday),
        'city': u'{city}'.format(city=city),
        'education': u'{education}'.format(education=education),
        'job': u'{job}'.format(job=job),
        'info': u'{info}'.format(info=info)
    }