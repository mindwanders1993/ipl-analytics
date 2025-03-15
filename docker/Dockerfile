FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements/prod.txt .
RUN pip install --no-cache-dir -r prod.txt

# Copy source code
COPY src/ ./src/
COPY configs/ ./configs/
COPY scripts/ ./scripts/

# Copy setup files
COPY setup.py .
COPY README.md .
COPY LICENSE .

# Install the package
RUN pip install -e .

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python", "-m", "src.main"]