FROM python:3.10-slim

# Устанавливаем только необходимые системные утилиты
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "--alluredir=allure-results"]
