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
ENV PYTHONPATH="/app/src"
RUN python -m unittest

# Setup links and permissions
RUN mkdir -p /root/.local/bin
ENV PATH="/root/.local/bin:$PATH"

RUN chmod +x ./src/service/items.py
RUN ln -s /app/src/service/items.py /root/.local/bin/item
RUN chmod +x ./src/service/tables.py
RUN ln -s /app/src/service/tables.py /root/.local/bin/table

