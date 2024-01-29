#!/usr/bin/python3
"""script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    args = sys.argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        args[1], args[2], args[3]
    ))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == args[4]).first()
    if query:
        print(f"{query.id}")
    else:
        print("Not found")

    session.close()
