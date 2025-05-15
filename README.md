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

> [!CAUTION]
> To completely delete the database delete the `pyventory_data` folder.
>
> Stopping the application won't delete the data.

## Database backup
The database is stored inside the `pyventory_data` folder.

Backing up that folder is enough to save your data.

To restore from backup replace the `pyventory_data` folder with your backup.

## Interacting with PyVentory Tables
(While the application is running :sweat_smile:)

For help run `docker compose exec pyventory table --help`

### READ ALL tables
`docker compose exec pyventory table -l` 

### CREATE a new table
`docker compose exec pyventory table -c <table name goes here>`

For example: `docker compose exec pyventory table -c pyventory`

### DELETE a table :warning:
`docker compose exec pyventory table -d <table name goes here>`

For example: `docker compose exec pyventory table -d pyventory`

## Interacting with PyVentory Items
(While the application is running :sweat_smile:)

For help run `docker compose exec pyventory item --help`

### READ ALL items
`docker compose exec pyventory item -l <table name goes here>` 

For example: `docker compose exec pyventory item -l pyventory` 

### READ a single item by ID
`docker compose exec pyventory item -l <table name goes here> -i <ID goes here>` 

For example: `docker compose exec pyventory item -l pyventory -i 1` 

### CREATE a new item
`docker compose exec pyventory item -c <table name goes here> -n <item name> -a <available amount>` 

For example: `docker compose exec pyventory item -c pyventory -n MyItem -a 5` 

### UPDATE an item
`docker compose exec pyventory item -c <table name goes here> -i <ID goes here> -n <item name> -a <available amount>` 

`item name` and `available amount` are both optional, but at least one is required.

For example: `docker compose exec pyventory item -c pyventory -i 1 -a 100`

To set the available amount of the item with ID 1 to 100

### DELETE a single item by ID :warning:
`docker compose exec pyventory item -d <table name goes here> -i <ID goes here>` 

For example: `docker compose exec pyventory item -d pyventory -i 1` 

