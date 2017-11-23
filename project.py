from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Victims, Vehicles, Crashes, Injuries


# initialize server and connect to database
app = Flask(__name__)
engine = create_engine("sqlite:///crashproject.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# displays index page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

	
# crashes page displays entire crashes table
@app.route('/crashes')
def crashes():
	crash = session.query(Crashes).all()
	return render_template('crashes.html', crashes = crash)


# victims page displays entire victims table	
@app.route('/victims')
def victims():
	victim = session.query(Victims).all()
	return render_template('victims.html', victims = victim)


# vehicles page displays entire vehicles table
@app.route('/vehicles')
def vehicles():
	vehicle = session.query(Vehicles).all()
	return render_template('vehicles.html', vehicles = vehicle)


# injuries page displays entire injuries table
@app.route('/injuries')
def injuries():
	injury = session.query(Injuries).all()
	return render_template('injuries.html', injuries = injury)


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)