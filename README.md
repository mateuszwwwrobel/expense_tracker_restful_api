# Expense Tracker - Flask Rest API
A flask-driven restful API for Expense Tracker application.


## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)** – Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. 
* **[Flask JWT Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)** – Flask-SQLAlchemy is an extension for Flask that adds basic JWT autentication. 
* **[Passlib](https://pypi.org/project/passlib/)** – Passlib is a password hashing library for Python 2 & 3, which provides cross-platform implementations of over 30 password hashing algorithms, as well as a framework for managing existing password hashes.


## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
Next thing to do is to clone the repository:

    ```sh
    $ https://github.com/mateuszwwwrobel/expense_tracker_restful_api.git
    ```

    Create a virtual environment to install dependencies in and activate it:

    ```sh
    $ python3 -m venv <venv-name>
    $ source <venv-name>/bin/activate
    ```

* #### Dependencies
    Then install the dependencies:

    ```sh
    (<venv-name>)$ pip install -r requirements.txt
  
    ```
* #### Config.py
    Open config.py and change a SQLALCHEMY_DATABASE_URI to correct path that match your system.

* #### Migrations
  
    Type following commands in your console to create a database and migrate it:
    ```
    (<venv-name>)$ flask db init
    ```
  
    Then, make and apply your Migrations
    ```
    (<venv-name>)$ flask db migrate -m "Initial migration."

    (<venv-name>)$ flask db upgrade
    ```


* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    (venv)$ python3 app.py
    ```
    You can now access the app on your local browser by using
    ```
    http://localhost:5000/expenses/
    ```
    Or test creating Expense using Postman
