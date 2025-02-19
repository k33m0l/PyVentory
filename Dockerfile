FROM python:3.13-slim

WORKDIR /app

COPY . /app

# Run tests
RUN python -m unittest

CMD ["python", "./src/main.py"]
