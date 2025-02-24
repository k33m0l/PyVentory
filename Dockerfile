FROM python:3.13-slim

# install psycopg2 dependencies
RUN apt-get update
RUN apt-get install -y libpq-dev gcc
RUN rm -rf /var/lib/apt/lists/*

# Install requirements
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app
# Run tests
RUN python -m unittest

# Start application
CMD ["python", "./src/main.py"]
