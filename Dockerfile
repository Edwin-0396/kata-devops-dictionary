# Base image with Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Add a non-root user
RUN useradd -m appuser
USER appuser

# Expose Prometheus metrics port
EXPOSE 8000

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8000/metrics || exit 1

# Run metrics server when container starts
CMD ["python", "metrics.py"]
