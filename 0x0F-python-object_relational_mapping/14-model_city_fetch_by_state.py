#!/usr/bin/python3
"""This module gets city by state"""

from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    host = 'localhost'
    port = '3306'
    State.cities = relationship("City",
                                order_by=City.id, back_populates="state")
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    eng = create_engine(connection.format(username, password, database),
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    query = session.query(State, City).filter(City.state_id == State.id).all()
    for row in query:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
