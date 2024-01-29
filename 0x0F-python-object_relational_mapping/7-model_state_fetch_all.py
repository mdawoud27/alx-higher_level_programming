#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    args = sys.argv

    # Create the connection to DB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        args[1], args[2], args[3]
    ))

    # Creating the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying and displaying the State objects
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    # Closing the session
    session.close()
