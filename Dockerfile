FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure temporary storage folders exist inside the container
RUN mkdir -p uploads static

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
