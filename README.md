# your-own-recipes
Web app to store recipes and make them live.

# Description

## Framework
Django Web application

## Technology and requirements
* python over 3.10
* pip
* poetry - handle packages
Python command launched via `make` will fail if the poetry is missing.

## Use the Makefile

A provided `Makefile` has several rules built to it. <br/>
`make help` gives you an overview of it.

## Virtualenv, pip and package

Before running the interpreter, make sure poetry is installed,
pyproject.toml exists and packages are installed:
```shell
make packages
```

## Database

### Create and run
Create database using a docker compose a basic docker image:
```shell
make db-start
```

### Connect to psql shell
```shell
make db-connect
```

## Application

Run the application using
```shell
make run
```
Make run should trigger manage.py makemigrations and manage.py migrate.

It is possible to call both using:
```shell
make db-makemigrations
make db-migrate
```