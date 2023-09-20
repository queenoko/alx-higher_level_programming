#!/usr/bin/python3
"""
The script that prints all City objects
from database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    This will give access to the database and get the cities
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_stateCal = State(name='California')
    sfr_cityCit = City(name='San Francisco')
    cal_stateCal.cities.append(sfr_cityCit)

    session.add(cal_stateCal)
    session.commit()
    session.close()
