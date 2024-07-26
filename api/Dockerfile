# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port on which the app will run
EXPOSE 5000

# Set environment variables
ENV MYSQL_PASSWORD=your_password
ENV MYSQL_DATABASE=ecommerce
ENV MYSQL_HOST=db

# Define the command to run the app
CMD ["python", "app.py"]