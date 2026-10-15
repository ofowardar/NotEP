# Python 3.10 base image
FROM python:3.10-slim

# Working directory
WORKDIR /app

# Kütüphaneleri kopyala
COPY requirements.txt .

# Kütüphaneleri kur
RUN pip install --no-cache-dir -r requirements.txt

# Kodları kopyala
COPY . .

# Port 8000'i expose et
EXPOSE 8000

# Sunucuyu başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]