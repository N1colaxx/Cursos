# img mais leve
FROM python:3.12-slim

WORKDIR /app

COPY . /app

# Instala somente as bibliotecas necessárias (sem cache para economizar espaço)
RUN pip install --no-cache-dir flask requests

EXPOSE 5000

CMD ["python", "app.py"]
