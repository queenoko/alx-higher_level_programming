#!/usr/bin/python3
"""
The script that lists all State objects
containing the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    This gives access to atabase and gets a state
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states1 = session.query(State).filter(State.name.contains('a'))
    if states1 is not None:
        for state in states1:
            print('{0}: {1}'.format(state.id, state.name))
