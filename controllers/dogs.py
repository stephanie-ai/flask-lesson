''' Dogs controller '''
from werkzeug.exceptions import BadRequest

dogs = [
    {'id': 1, 'name': 'Bob', 'age': 2},
    {'id': 2, 'name': 'Oscar', 'age': 5},
    {'id': 3, 'name': 'Milo', 'age': 4}
]

def index(req):
    return [d for d in dogs], 200

def show(req,uid):
    return find_by_uid(uid),200

def create(req):
    new_cat = req.get_json()
    new_cat['id'] = sorted (d ['id'] for d in dogs]) [-1]
    dogs.append(new_dog)
    return new_dog, 201


def update(req, uid):
    dog = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        dog[key] = val
    return dog, 200

def destroy(req, uid):
    dog = find_by_uid(uid)
    dogs.remove(cat)
    return dog, 204

def find_by_uid(uid):
    try:
        return next(dog for dog in dog if dog['id'] == uid)
    except:
        raise BadRequest(f"We don't have that dog with id {uid}!")

