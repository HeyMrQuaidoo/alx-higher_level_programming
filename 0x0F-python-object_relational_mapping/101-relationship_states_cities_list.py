#!/usr/bin/python3
""" This module lists all states and their
corresponding cities
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State, Base
from relationship_city import City
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    host = 'localhost'
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                            username, password, host, port, database
                            ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    data = session.query(State).order_by(State.id).all()

    for row in data:
        print("{}: {}".format(row.id, row.name))
        for city in row.cities:
            print("    {}: {}".format(city.id, city.name))

    session.commit()
    session.close()
