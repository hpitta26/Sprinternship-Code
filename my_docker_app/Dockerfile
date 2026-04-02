# Use the official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application source into the image
COPY app.py .

# Document that the container listens on port 8080
EXPOSE 8080

# Command to run when the container starts
CMD ["python", "app.py"]
