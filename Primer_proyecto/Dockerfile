# 1. Usamos una imagen oficial de Python como base
FROM python:3.12-slim

# 2. Creamos un directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos todo el contenido de tu proyecto al contenedor 
COPY . /app

# 4. Instalamos Flask dentro del contenedor
RUN pip install flask

# 5. Definimos el comando para arrancar tu aplicación
CMD ["python", "app.py"]
