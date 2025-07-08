# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port FastAPI will run on
EXPOSE 8000

# Start the app
CMD ["uvicorn", "medical_chatbot_api:app", "--host", "0.0.0.0", "--port", "8000"]
