from flask import Flask, render_template, jsonify, request, redirect, url_for, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Victims, Vehicles, Crashes, Injuries


# initialize server and connect to database
app = Flask(__name__)
engine = create_engine("sqlite:///crashproject.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


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


@app.route('/view1')
def view1():
	view = session.query(Victims).join(Vehicles, Vehicles.vehicleid==Victims.vehicleid).join(Crashes, Crashes.crashno==Victims.crashno).add_columns(Victims.fname, Victims.lname, Vehicles.vehicleid, Crashes.crashdate).all()
	return render_template('view1.html', view1 = view)

	
#@app.route('/view2')
#def view2():
#	return render_template('view2.html', view2 = view)


@app.route('/view3')
def view3():
	sub = session.query(Crashes.crashcity).filter(Crashes.crashcity == Victims.city).subquery()
	view = session.query(Victims).filter(Victims.city == sub).all()
	return render_template('view3.html', view3 = view)


#@app.route('/view4')
#def view4():
#	return render_template('view4.html', view4 = view)


@app.route('/view5')
def view5():
	sub = session.query(Crashes.crashcity).filter(Crashes.crashcity == Victims.city).subquery()
	qry1 = session.query(Victims).add_columns(Victims.fname, Victims.lname, Victims.crashno, Victims.dob, Victims.gender, Victims.city).filter(sub == Victims.city)
	qry2 = session.query(Victims).add_columns(Victims.fname, Victims.lname, Victims.crashno, Victims.dob, Victims.gender, Victims.city).filter(Victims.gender == 'F')
	view = qry1.union(qry2)
	return render_template('view5.html', view5 = view)


@app.route('/view6')
def view6():
	view = session.query(Victims, Crashes).add_columns(Victims.fname, Victims.lname, Crashes.crashno, Victims.victimid, Crashes.location).filter(Crashes.crashno == Victims.crashno, Crashes.crashtime == 'Morning').all()
	return render_template('view6.html', view6 = view)


@app.route('/view7')
def view7():
	view = session.query(Victims).filter(Vehicles.vehicleid == Victims.vehicleid, Vehicles.make == 'Toyota').all()
	return render_template('view7.html', view7 = view)


@app.route('/view8')
def view8():
	view = session.query(Vehicles, Victims).add_columns(Vehicles.lplate, Vehicles.make, Vehicles.model, Victims.fname, Victims.lname).filter(Vehicles.vehicleid == Victims.vehicleid).all()
	return render_template('view8.html', view8 = view)


@app.route('/view9')
def view9():
	view = session.query(Victims, Vehicles, Crashes).add_columns(Victims.vehicleid, Victims.fname, Victims.lname, Vehicles.make, Vehicles.model).filter(Crashes.crashno == Victims.crashno, Victims.vehicleid == Vehicles.vehicleid, Crashes.crashtime == 'Night').all()
	return render_template('view9.html', view9 = view)


@app.route('/view10')
def view10():
	view = session.query(Victims, Vehicles, Injuries).add_columns(Victims.victimid, Victims.fname, Victims.lname, Vehicles.make, Vehicles.model, Injuries.fatality).filter(Injuries.crashno == Victims.crashno, Vehicles.vehicleid == Victims.vehicleid, Injuries.injurytype == 'Back').all()
	return render_template('view10.html', view10 = view)


# create simple api that takes in crashnumber and response with crash details of said crash
# ex http://localhost:5000/api/2003
@app.route('/api/<crashnumber>')
def crashesJSON(crashnumber):
	crashes = session.query(Crashes).filter_by(crashno = crashnumber).one()
	return jsonify(crashes = crashes.serialize)
	

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)