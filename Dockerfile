FROM python:3.10-slim

WORKDIR /app

# sin esto no funca la conexion a la BD, el rm elimina la cache de la instalacion 
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]



