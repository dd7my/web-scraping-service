FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Upgrade pip and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the API port
EXPOSE 5000

# Set environment variables (these can be overridden at runtime)
ENV FLASK_ENV=production
ENV PORT=5000

# Command to run the Waitress production server
CMD ["python", "app.py"]
