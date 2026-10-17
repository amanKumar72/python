from sqlmodel import SQLModel, create_engine, Session

connection_string: str = "sqlite:///rangmanch.db"
engine = create_engine(connection_string, echo=True)

def create_tables():
    """Create all tables defined by the SQLModel classes in the database"""
    SQLModel.metadata.create_all(engine)

def get_session():
    '''dependency that provide a db session per request'''
    with Session(engine) as session:
        yield session
    