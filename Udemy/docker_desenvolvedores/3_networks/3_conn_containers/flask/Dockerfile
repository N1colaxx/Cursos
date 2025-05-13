# img mais leve
FROM python:3.12

WORKDIR /app

COPY . /app

# Instala somente as bibliotecas necessárias (sem cache para economizar espaço)
RUN pip install  flask requests flask_mysqldb 

EXPOSE 5000

CMD ["python", "app.py"]

