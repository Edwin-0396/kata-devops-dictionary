# Base image with Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install runtime deps
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Expose Prometheus metrics port
EXPOSE 8000

# Add HEALTHCHECK
HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1

# Run as non-root user
RUN useradd -m appuser
USER appuser

# Start the app
CMD ["python", "metrics.py"]
