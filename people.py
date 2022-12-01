from datetime import datetime

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