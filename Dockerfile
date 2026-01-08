# Use Python 3.10 (compatible with sklearn 1.2.2)
FROM python:3.10.13-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Start Flask app using gunicorn
CMD ["gunicorn", "app:app"]
