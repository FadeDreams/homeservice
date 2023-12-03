
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# Install any needed packages specified in requirements.txt
# RUN apt-get update \
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=core.settings.dev

# Collect static files
RUN python3 manage.py collectstatic --noinput

# Run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
