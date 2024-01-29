#!/usr/bin/python3
""""""
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first_name, last_name, gender, age):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.first_name} {self.last_name} ({self.gender}, {self.age})"


class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

person = Person(403080, "Mohamed", "Dawoud", "m", 21)
session.add(person)
session.commit()

p1 = Person(403010, "Mohamed", "Gamal", "m", 23)
p2 = Person(403020, "Angela", "Dan", "f", 31)
p3 = Person(403030, "Fares", "Mostafa", "m", 19)
p4 = Person(403040, "Anna", "Elsayed", "f", 30)
session.commit()
# p
session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)

result = session.query(Person).filter(Person.first_name == "Mohamed")
for r in result:
    print(r)

t1 = Thing(1, "Car", p1.ssn)
session.add(t1)
session.commit()
