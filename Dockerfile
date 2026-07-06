FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# --- NEW: Natively create the Streamlit config inside the container ---
RUN mkdir -p .streamlit && \
    echo '[server]' > .streamlit/config.toml && \
    echo 'port = 8080' >> .streamlit/config.toml && \
    echo 'address = "0.0.0.0"' >> .streamlit/config.toml && \
    echo 'enableCORS = false' >> .streamlit/config.toml && \
    echo 'enableXsrfProtection = false' >> .streamlit/config.toml

EXPOSE 8080

# Clean execution call
ENTRYPOINT ["streamlit", "run", "app.py"]
