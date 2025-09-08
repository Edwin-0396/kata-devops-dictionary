# Base image with Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Expose Prometheus metrics port
EXPOSE 8000

# Run metrics server when container starts
CMD ["python", "metrics.py"]
