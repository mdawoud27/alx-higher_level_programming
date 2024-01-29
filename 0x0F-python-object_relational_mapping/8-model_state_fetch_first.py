#!/usr/bin/python3
"""script that prints the first State object
from the database hbtn_0e_6_usa
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

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
