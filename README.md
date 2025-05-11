# PyVentory

> [!CAUTION]
> This is a learning project that will help me become familiar with Python, and it is :construction: under construction :construction:.
>
> Once I have tried out everything I want, it will be abandoned and archived.

## Requirements
* Docker
* Docker Compose

## Before first launch
Please update the default database user and password in the [.env](.env) file!

## Starting PyVentory
To start the service with docker compose you simply have to run: `docker compose up --build -d` from the root folder.
This will start both PyVentory and the required database in detached mode.
You'll see when the service is ready, it takes about 10 seconds for everything to start.

## Stopping PyVentory
Once you're done using PyVentory, you simple have to run `docker compose down` from the root folder.

> !CAUTION
> To completely delete the database delete the `pyventory_data` folder.
> Stopping the application won't delete the data.

## Database backup
The database is stored inside the `pyventory_data` folder.
Backing up that folder is enough to save your data.
To restore from backup replace the `pyventory_data` folder with your backup.

## Interacting with PyVentory
(While the application is running :sweat_smile:)
### READ ALL
TEMP: `docker compose exec PyVentory items` 

