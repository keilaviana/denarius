from fastapi import FastAPI
from app import Base, engine

#docker-compose up --build
#docker-compose down

# Teste acesso ao backend:      http://127.0.0.1:8000/

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "O backend do Denarius está ativado!"}

# Cria as tabelas do bd
Base.metadata.create_all(bind=engine)

# reset uvicorn
#cd backend
#.\venv\Scripts\activate
# Executar o servidor:          uvicorn app.main:app --reload