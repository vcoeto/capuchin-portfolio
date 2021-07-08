# Pod 3.3.5 Mongo Monkeys 
Team 4 - Capuchin Monkeys
---

##### Participants:
1. *Anthony Jimenez*
2. *Victor Coeto*
3. *Joying yang*

---
## General Aspects

This documents serves as a guide to the implementation of a flask application to create a personal portfolio with different pages using html, css, bootstrap running on a flask server.

### Technical requirements

* Freedom of use
* Use of Flask 


### Structure of the files
```
- / 			        # Root of the project
    -README.md		    # Description, usage and installation of the template
    -License.txt        # Open Source License for ther project
    -example.env        # Where the server of flask will run 
    -License.txt        # Libraries required for the app to work
    -app                # Where all the app components are located
        -__init__.py    # Main flask file with the existing routes
        -nav.py         # Python file for the navigation name
        -templates	    # All HTML files
        -static         # img, js and styles folders for the HTML
```


## Frontend
* Bootstrap
* HTML
* CSS

#### Libraries or dependencies
* Bootstrap


## Backend
* Python

#### Libraries or dependencies
* click==8.0.1
* Flask==2.0.1
* itsdangerous==2.0.1
* Jinja2==3.0.1
* MarkupSafe==2.0.1
* python-dotenv==0.17.1
* Werkzeug==2.0.1
* flask_nav==0.6




# Installation & Usage

Make sure you have python3 and pip installed

## Windows
Creating the virtual environment
```
py -3 -m venv python3-virtualenv

python3-virtualenv\Scripts\activate
```
After the environment was created, we need to install the necesaries dependencies
Installing the requirements
```
pip install -r requirements.txt
```
Start flask development server
```
set FLASK_ENV=development
flask run
```

## Linux / Mac

Creating the virtual environment
```
$ python3 -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```
Installation of the dependencies

```
pip install -r requirements.txt
```
Start flask development server
```
export FlASK_ENV=development
flask run
```

## Docker usage 

for this part we will be using the dockerfile, it's important to have this information: 

```
FROM python:3.8-slim-buster

RUN mkdir /myportfolio
COPY requirements.txt /myportfolio
WORKDIR /myportfolio
RUN pip3 install -r requirements.txt
COPY . /myportfolio
CMD [ "gunicorn", "wsgi:app", "-w 4", "-b 0.0.0.0:80" ]
```
Also remove from the requirements dataclases, if exists. After having that docker file we'll run these commands to create the container and then run it. 

```
docker build -t myportfolio:0.0.1 .
```

```
docker run -p 81:80 myportfolio:0.0.1
```
NOW IT WILL BE ACCESSIBLE FROM http://127.0.0.1:81/

If we want to use the docker compose is with 

```
docker-compose up --build 
```
the migrations folder is done by the command to use the sqlalchemy
``` 
flask db init
```
## References 
* https://flask-pymongo.readthedocs.io/en/latest/
