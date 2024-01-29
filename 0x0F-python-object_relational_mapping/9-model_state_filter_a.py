#!/usr/bin/python3
"""script that lists all State objects that contain the letter `a`
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    args = sys.argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        args[1], args[2], args[3]
    ))

    Session = sessionmaker(bind=engine)
    session = Session()

    rows_with_a = session.query(State).order_by(State.id).filter(
        State.name.like("%a%"))
    # print(rows_with_a)
    for row in rows_with_a:
        print(f"{row.id}: {row.name}")
    session.close()
