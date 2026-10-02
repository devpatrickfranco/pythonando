from models import Cursos, engine
from sqlmodel import Session, select, or_


with Session(engine) as session:
    statement = select(Cursos).limit(3)
    results = session.exec(statement).all()
    print(results)