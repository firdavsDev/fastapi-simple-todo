# Dockerfile
FROM python:3.9-slim

# O'rnatish uchun zarur paketlar
RUN apt-get update && apt-get install -y libpq-dev

# Ishchi papkaga o'zgartirish
WORKDIR /app

# Talablarni o'rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Dastur fayllarini nusxalash
COPY . /app

# Uvicornni ishga tushurish
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "app/core/logging.conf", "--workers", "4"]

