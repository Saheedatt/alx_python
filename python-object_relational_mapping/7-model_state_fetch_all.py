"""
Script to list all State objects from the hbtn_0e_6_usa database.

This module inherits from the previously built model_state.py.
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

def list_states(username, password, database):
    """
    Fetches and lists all State objects from the hbtn_0e_6_usa database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
    Returns:
        None
    """
    # Create the connection URL
    connection_url = 'mysql://{0}:{1}@localhost:3306/{2}'.format(username, password, database)
    # Create the SQLAlchemy engine
    engine = create_engine(connection_url)

    # Bind the engine to the Base
    Base.metadata.bind = engine

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Now, query and list all State objects sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{0}: {1}".format(state.id, state.name))

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
