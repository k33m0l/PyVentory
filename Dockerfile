FROM python:3.13-slim

# Install requirements
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app
# Run tests
RUN python -m unittest

# Start application
CMD ["python", "./src/main.py"]
