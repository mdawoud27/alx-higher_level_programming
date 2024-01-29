#!/usr/bin/python3
"""script that changes the name of a State object
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

    mexico_state = session.query(State).filter_by(id=2).first()
    mexico_state.name = "New Mexico"

    session.commit()
    session.close()
