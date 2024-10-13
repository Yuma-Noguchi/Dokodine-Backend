# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

ENV PORT=8080

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /code
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that FastAPI will run on
EXPOSE ${PORT}

# Command to run the FastAPI application
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]