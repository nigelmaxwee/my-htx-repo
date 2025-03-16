# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy required files to the container
COPY asr_api.py requirements.txt ./

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8001 for FastAPI
EXPOSE 8001

# Run the API using Uvicorn
CMD ["uvicorn", "asr_api:app", "--host", "0.0.0.0", "--port", "8001"]
