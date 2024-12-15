# Usar a imagem oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar apenas o arquivo de dependências primeiro
COPY requirements.txt /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o container
COPY . /app

# Expôr a porta em que o FastAPI irá rodar
EXPOSE 8000

# Definir o comando de execução para rodar o FastAPI com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
