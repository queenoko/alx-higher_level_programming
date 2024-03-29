#!/usr/bin/python3
"""
This script will lists all State objects and its
corresponding City objects contained in the DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    stList = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for stateLi in stList:
        print("{}: {}".format(stateLi.id, stateLi.name))
        for city in stateLi.cities:
            print("    {}: {}".format(city.id, city.name))
