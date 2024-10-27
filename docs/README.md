# W4153-P1-Application

The link to the repository is: https://github.com/donald-f-ferguson/W4153-P1-Application

## Overview

Project 1 in W4153 - Cloud Computing is to build a simple [fullstack web application.](https://medium.com/@p.reaboi.frontend/understanding-full-stack-development-architecture-a-comprehensive-guide-548f8cba6d91)

This project is the application/business logic project. It is a
[FastAPI](https://fastapi.tiangolo.com/) application.

|   <img src="fullstack.jpg">   |
|:-----------------------------:|
| __Fulltsack Web Application__ |


## Installation

You must create a new [Python virtual environment](https://docs.python.org/3/library/venv.html) for this application.
I use [PyCharm](https://www.jetbrains.com/pycharm/), and I recommend that you do the same. You
can follow the [PyCharm instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) for creating a virtual environment for your project.
Open a terminal window in the virtual environment and enter

```pip install -r requirements.txt```

You will see several information and warning messages, and you can ignore them. As long as
you did not get fatal errors, your installation worked.

## Running the Application

Follow the PyCharm instructions for running the application. You will see something that looks like

<img src='apprun.jpg'>

Click on the URL or copy/paste and open in a browser. You will see something that
looks like

<img src="ui1.jpg">

In the browser, navigate to ```http://0.0.0.0:8000/docs``` You will see something like

<img src="ui2.jpg">

If you see this page, you are done for now.

TODO: Understand how you go from object data model into hitting DB from API request

Models = objects that will be populated with data from the QB query 

Resources = wrapper for how to call the DB, make the different 
query wrappers here, like insert, update, search, etc. 

Routers = defining the routes for each specific model aka table into 
the DB, here define the different routes that are hittable by the user 
given API requests 

Service factory = creates the connection to the Database,
 so maybe you can define the different connections to other DBs or microservices?
# TODO: how to handle connecting to other APIs and making requests 




