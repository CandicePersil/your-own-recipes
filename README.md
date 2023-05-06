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

A provided `Makefile` has several rules built to it.
`make help` gives you an overview of it.

## Virtualenv, pip and package

Before running the interpreter, make sure poetry is installed,
pyproject.toml exists and packages are installed (make packages).

## Database

Create database in a docker and use a docker compose ?
Kube ?