# Use an official Python runtime as the base image
FROM python:3.11
LABEL authors="kwarteng"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install MongoDB client libraries
RUN apt-get update && apt-get install -y libcurl4 openssl

# Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN pip install pytz six

# Install NLTK data
RUN python -m nltk.downloader punkt averaged_perceptron_tagger

# Copy the project files into the container
COPY . .

# Run migrations and collect static files
#RUN python manage.py makemigrations
#RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pdf_processor.wsgi:application"]