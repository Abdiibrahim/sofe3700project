# SOFE 3700U - Final Project - Group 22
Application that stores vehicle accident data in a SQLite database, acts as a web server, and creates a REST API to serve JSON files. Utilizes Google's GoogleMaps API to display city locations of crashes.

# Windows Setup
- Install git [if not already installed](https://git-scm.com/download/win)
- Install [Python 2.7](https://www.python.org/downloads/release/python-2712/)
- Add Python and Python scripts to path variable
- Install dependencies
- More documentation on [venv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

- Command-line instructions:
```
pip install virtualenv virtualenvwrapper
virtualenv venv
venv\scripts\activate
pip install -r requirements.txt
deactivate
```

### DB Browser for SQLite Setup (optional)
- Install [DB Browser for SQLite](http://sqlitebrowser.org/)
- Follow install instructions.
- Click open database and select database file

## Running Project
- Run the Virtual Envirionment in the project folder via command-line
- run database_setup.py to create the database
- run populate.py to add data to database
- run project.py to run app on the webserver
- Open [localhost:5000](http://localhost:5000/) in your web browser

```
venv\scripts\activate
python database_setup.py
python populate.py
python project.py
```
# Special Mentions
rochacbruno's [Flask-googlemaps](https://github.com/rochacbruno/Flask-GoogleMaps)
