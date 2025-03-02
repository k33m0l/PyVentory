# PyVentory
:construction: Under construction :construction:

## Requirements
* Docker
* Docker Compose

## Before first launch
Please update the default database user and password in the [.env](.env) file!
Create a folder called `pyventory_data`
Create a docker volume named "pyventory_data" using `docker volume create pyventory_data --driver local --opt "type=none" --opt "device=$PWD/pyventory_data" --opt "o=bind"`

## Starting PyVentory
To start the service with docker compose you simply have to run: `docker compose up --build -d` from the root folder.
This will start both PyVentory and the required database in detached mode.

## Stopping PyVentory
Once you're done using PyVentory, you simple have to run `docker compose down` from the root folder.

## Interacting with PyVentory
TODO