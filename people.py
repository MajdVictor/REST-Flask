from datetime import datetime
from flask import abort

def get_timestamp():
    '''
    helper functionin returns recent timestamp
    '''
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Majd": {
        "fname": "Majd",
        "lname": "Hafiri",
        "timestamp": get_timestamp(),
    },
    "George": {
        "fname": "George",
        "lname": "Hafiri",
        "timestamp": get_timestamp(),
    },
    "Charlie": {
        "fname": "Charlie",
        "lname": "Hafiri",
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(PEOPLE.values())

def create(person):
    lname = person.get("lname")
    fname = person.get("fname")

    if (lname and lname) not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )

def read_one(fname):
    if fname in PEOPLE:
        return PEOPLE[fname]

    abort(404, f"person with last name {fname} not found!")

def update(fname, person):
    if fname in PEOPLE:
        PEOPLE[fname]["lname"] = person.get("lname")
        PEOPLE[fname]["timestamp"] = get_timestamp()
        return PEOPLE[fname], 202
    abort(404, f"person {fname} not found in dict")

def delete(fname):
    if fname in PEOPLE:
        del PEOPLE[fname]
        return f"{fname} Deleted successfully", 200
    abort(404, f" {fname} Not found!")