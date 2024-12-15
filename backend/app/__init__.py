import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Rodar o código: uvicorn app.main:app --reload

load_dotenv()

# Obter URL do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")

# Configurar o SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Criar uma sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Dependência para obter a sessão do banco em rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
