from sqlmodel import Session, create_engine
from fastapi import Depends
from typing import Annotated 

sqlite_name = 'db.sqlite3'
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url)

# Conectandonos a una bd
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]