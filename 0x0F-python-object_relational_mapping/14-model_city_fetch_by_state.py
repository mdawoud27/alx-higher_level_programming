#!/usr/bin/python3
"""Script  that prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    args = sys.argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        args[1], args[2], args[3]
    ))

    Session = sessionmaker(bind=engine)
    session = Session()

    state_query = session.query(State).order_by(State.id).all()
    city_query = session.query(City).order_by(City.id).all()
    for state in state_query:
        for city in city_query:
            if state.id == city.state_id:
                print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
