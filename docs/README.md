# Professor Microservice

This repository is meant to allow for the access of professor information stored
in a dedicated professor SQL database. This microservice is built on the data
model that the Professor only has a UNI, First Name and Last Name. In further sprints, 
we will be able to expand on this data model to include more information like a middle name, department,
etc. 

## Overview

FastAPI for our route handling framework and MySQL used for the databases (DB). 
The DB wrapper for going from python to SQL queries is reverse engineerable starting
from ```MySQLRDDBDataService.py``` file. You can find the OpenAPI spec 
when you launch the application and visit the /docs/ endpoint. 

To launch the microservice, utilize the command ```fastapi run``` and, 
for restarting the server after file changes in development, I use ```fastapi run --reload```. 

## Installation

For local testing, I suggest DataGrip to allow for an easier time setting up 
your database and actually visualizing what the table rows look like. 
I use VS Code for the development of this microservice. 

## Running the Application

Simply enable the virtual environment for the virtual machine you are in. First make 
the virtual environment using: ```python -m venv```, then
activate your venv using ```source venv/bin/activate```. 
Get all python dependencies using ```pip install -r requirements.txt```. 
Then, you need to populate these following environment variables to configure
the utilized database:
- DB_USER=Username to access MySQL DB 
- DB_PASSWORD=Password to access MySQL DB 
- DB_HOST=Input either URL to the Cloud SQL instance or just use localhost for locally testing
- DB_PORT=Default set to 3306 but change it accordingly to the Cloud SQL instance 




