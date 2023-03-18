#!/usr/bin/python3
"""script that prints the first state object"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.id).filter(State.name == sys.argv[4]).first()
    if (query):
        print(query[0])
    else:
        print("Not found")
    session.close()
