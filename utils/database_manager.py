from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_database_session(database_url: str):
    engine = create_engine(database_url, echo=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    return session