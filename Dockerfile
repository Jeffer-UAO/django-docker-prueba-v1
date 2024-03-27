#Etapa 1: Construcción del proyecto Django
FROM python:3.10 AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Configura las variables de entorno si es necesario
# ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Ejecuta los comandos de construcción, por ejemplo, migraciones y recolección de archivos estáticos
# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate
# RUN python3 manage.py collectstatic --no-input

# Etapa 2: Despliegue a producción
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /app .

# Configura las variables de entorno si es necesario
# ENV DJANGO_SETTINGS_MODULE=myproject.settings

RUN pip install gunicorn
EXPOSE 8000

# Comando para arrancar el servidor web, por ejemplo, con gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]