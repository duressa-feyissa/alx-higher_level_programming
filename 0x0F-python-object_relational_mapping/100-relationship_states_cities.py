#!/usr/bin/python3
"""
    a script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""

from sqlalchemy.engine.url import URL
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    from sqlalchemy.engine import create_engine
    from sqlalchemy.engine.url import URL
    from sqlalchemy.orm import Session
    from relationship_city import City
    from relationship_state import Base, State
    from sys import argv

    db = {'drivername': 'mysql+mysqldb',
          'host': 'localhost',
          'port': '3306',
          'username': argv[1],
          'password': argv[2],
          'database': argv[3]}

    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    city = City(name='San Francisco')
    state = State(name='California', cities=[city])

    session.add(state)
    session.add(city)
    session.commit()
    session.close()
