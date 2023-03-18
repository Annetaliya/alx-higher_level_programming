#!/usr/bin/python3
"""script that prints the first state object"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine, desc


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    query = session.query(State.id).order_by(State.id.desc()).first()
    if (query):
        print(query[0])
    session.close()
