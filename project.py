from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Victims, Vehicles, Crashes, Injuries


# initialize server
app = Flask(__name__)
engine = create_engine("sqlite:///crashproject.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/crashes')
def crashes():
	crash = session.query(Crashes).all()
	return render_template("crashes.html", crashes = crash)
	
@app.route('/victims')
def victims():
	victim = session.query(Victims).all()
	return render_template('victims.html', victims = victim)


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)