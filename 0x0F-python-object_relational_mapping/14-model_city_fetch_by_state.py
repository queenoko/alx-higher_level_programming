#!/usr/bin/python3
"""
The script that prints all City objects
from the database `hbtn_0e_14_usa..`.
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    This gives access to database and get the cities
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    resultsSt = session.query(City, State).join(State)

    for city1, state in resultsSt.all():
        print("{}: ({}) {}".format(state.name, city1.id, city1.name))

    session.commit()
    session.close()
