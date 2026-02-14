# Use Python as the base image
FROM python:3.14-slim

# Set working directory inside the container
WORKDIR /app

# Copy your web app into the container
COPY my_first_webapp.py .

# Install Flask
RUN pip install flask

# Expose port 5000 (where Flask runs)
EXPOSE 5000

# Command to run when container starts
CMD ["python", "my_first_webapp.py"]
