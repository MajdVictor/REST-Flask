from flask import abort, make_response
from config import db
from models import Person, people_schema, person_schema

def read_all():

    people = Person.query.all()
    return people_schema.dump(people)

def read_one(fname):

    person = Person.query.filter(Person.fname == fname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"person with first name {fname} not found!")


def create(fname, person):
    print(person)
    fname = person.get("fname")
    existing_person = Person.query.filter(Person.fname == fname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(406, f"Person with first name {fname} already exists")

  
def update(fname, person):
    existing_person = Person.query.filter(Person.fname == fname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.lname = update_person.lname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(404, f"Person with first name {fname} not found")

def delete(fname):
    existing_person = Person.query.filter(Person.fname == fname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{fname} successfully deleted", 200)
    else:
        abort(404, f"Person with first name {fname} not found")