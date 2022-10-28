#!/usr/bin/python3
"""
    a script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.name.like('%a%')).all()
    for i in res:
        session.delete(i)
    session.commit()
