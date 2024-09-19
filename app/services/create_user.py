from database import firebase
from models.constants import collection

def create_user(username: str, usersurname: str, user_tid: str, gender: str, birthday: str, city: str, education: str, job: str, info: str, subscription: bool, purpose: bool):
    print("entered to services")
    firebase.database.collection(u'{collection}'.format(collection=collection)).document(u'{user_tid}'.format(user_tid=user_tid)).set({
        u'username': u'{username}'.format(username=username),
        u'usersurname': u'{usersurname}'.format(usersurname=usersurname),
        u'user_tid': u'{user_tid}'.format(user_tid=user_tid),
        u'gender': u'{gender}'.format(gender=gender),
        u'birthday': u'{birthday}'.format(birthday=birthday),
        u'city': u'{city}'.format(city=city),
        u'education': u'{education}'.format(education=education),
        u'job': u'{job}'.format(job=job),
        u'info': u'{info}'.format(info=info),
        u'subscription': u'{subscription}'.format(subscription=subscription),
        u'purpose': u'{purpose}'.format(purpose=purpose),
    })
    
    return {
        'id': user_tid,
        'username': '{username}'.format(username=username),
        'usersurname': u'{usersurname}'.format(usersurname=usersurname),
        'user_tid': u'{user_tid}'.format(user_tid=user_tid),
        'gender': '{gender}'.format(gender=gender),
        'birthday': '{birthday}'.format(birthday=birthday),
        'city': u'{city}'.format(city=city),
        'education': u'{education}'.format(education=education),
        'job': u'{job}'.format(job=job),
        'info': u'{info}'.format(info=info),
        'subscription': u'{subscription}'.format(subscription=subscription),
        'purpose': u'{purpose}'.format(purpose=purpose),
    }


def create_user_rent(user_tid: str, purpose_rent: str, country: str, city: str, status: str
    ,month_budget: str, region: str, photos: str, dates: str):
    print("entered to firebase subcollection creating for rent")

    user_ref = firebase.database.collection(u'{collection}'.format(collection=collection)).document(u'{user_tid}'.format(user_tid=user_tid))

    user_ref.collection('rent_purpose').document(u'{user_tid}'.format(user_tid=user_tid)).set({
        u'purpose_rent': u'{purpose_rent}'.format(purpose_rent=purpose_rent),
        u'country': u'{country}'.format(country=country),
        u'city': u'{city}'.format(city=city),
        u'status': u'{status}'.format(status=status),
        u'month_budget': u'{month_budget}'.format(month_budget=month_budget),
        u'region': u'{region}'.format(region=region),
        u'photos': u'{photos}'.format(photos=photos),
        u'dates': u'{dates}'.format(dates=dates),

    })

    return {
        'purpose_rent': u'{purpose_rent}'.format(purpose_rent=purpose_rent),
        'country': u'{country}'.format(country=country),
        'city': u'{city}'.format(city=city),
        'status': u'{status}'.format(status=status),
        'month_budget': u'{month_budget}'.format(month_budget=month_budget),
        'region': u'{region}'.format(region=region),
        'photos': u'{photos}'.format(photos=photos),
        'dates': u'{dates}'.format(dates=dates),
    }

def create_user_travel(user_tid: str, purpose_travel: str, country: str, city: str, status: str,dates: str, longness: str, day_budget: str):
    print("entered to firebase subcollection creating for rent")

    user_ref = firebase.database.collection(u'{collection}'.format(collection=collection)).document(u'{user_tid}'.format(user_tid=user_tid))

    user_ref.collection('travel_purpose').document(u'{user_tid}'.format(user_tid=user_tid)).set({
        u'purpose_travel': u'{purpose_travel}'.format(purpose_travel=purpose_travel),
        u'country': u'{country}'.format(country=country),
        u'city': u'{city}'.format(city=city),
        u'status': u'{status}'.format(status=status),
        u'dates': u'{dates}'.format(dates=dates),
        u'longness': u'{longness}'.format(longness=longness),
        u'day_budget': u'{day_budget}'.format(day_budget=day_budget),
    })

    return {
        'purpose_travel': u'{purpose_travel}'.format(purpose_travel=purpose_travel),
        'country': u'{country}'.format(country=country),
        'city': u'{city}'.format(city=city),
        'status': u'{status}'.format(status=status),
        'dates': u'{dates}'.format(dates=dates),
        'longness': u'{longness}'.format(longness=longness),
        'day_budget': u'{day_budget}'.format(day_budget=day_budget),
    }