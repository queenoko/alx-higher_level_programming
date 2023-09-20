#!/usr/bin/python3
"""
The script that adds State object
`Louisiana` to database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    This gives access to database and get a state
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_stateLo = State(name="Louisiana")
    session.add(new_stateLo)
    session.commit()

    print('{0}'.format(new_stateLo.id))
    session.close()
