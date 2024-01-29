#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter 'a'
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

    del_states_a = session.query(State).filter(State.name.like("%a%"))

    # Delete the selected states
    del_states_a.delete(synchronize_session=False)

    session.commit()
    session.close()
