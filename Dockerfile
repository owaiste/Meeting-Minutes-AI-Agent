FROM python:3.11-slim

WORKDIR /app

# Removed software-properties-common to fix the build crash
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements FIRST so Docker can cache your dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

EXPOSE 8080

ENTRYPOINT streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
