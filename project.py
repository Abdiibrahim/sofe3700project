from flask import Flask, render_template, jsonify, request, redirect, url_for, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Victims, Vehicles, Crashes, Injuries
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


# initialize server and connect to database
app = Flask(__name__)
# access google maps API with API key
app.config['GOOGLEMAPS_KEY'] = "AIzaSyBgjSr2wdxq3G9H7zOkemX3Fl1hwe2y4gc"
GoogleMaps(app, key="AIzaSyBgjSr2wdxq3G9H7zOkemX3Fl1hwe2y4gc")
# start session with the database
engine = create_engine("sqlite:///crashproject.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# render index page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


# render maps page based on the crashno. Will mark the city of the crash based on latitude and longitude information
@app.route('/crashes/map/<crashnumber>')
def crashmap(crashnumber):
	crash = session.query(Crashes).add_columns(Crashes.crashlat, Crashes.crashlng, Crashes.crashno, Crashes.crashcity).filter_by(crashno = crashnumber).one()
	# creating a map in the view
	mymap = Map(
		identifier="view-side",
		lat=crash[1],
		lng=crash[2],
		zoom=10,
		markers=[(crash[1], crash[2])]
	)
	return render_template('map.html', mymap=mymap, crash=crash) 

	
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


# displays view1 table from query
# Returns fname, lname, vehicleid and crashdate of all victims
@app.route('/view1')
def view1():
	view = session.query(Victims).join(Vehicles, Vehicles.vehicleid==Victims.vehicleid).join(Crashes, Crashes.crashno==Victims.crashno).add_columns(Victims.fname, Victims.lname, Vehicles.vehicleid, Crashes.crashdate).all()
	return render_template('view1.html', view1 = view)

	
#@app.route('/view2')
#def view2():
#	return render_template('view2.html', view2 = view)


# Returns crashno, fname, lname, city where the crashcity and victim's city are the same
@app.route('/view3')
def view3():
	sub = session.query(Crashes.crashcity).filter(Crashes.crashcity == Victims.city).subquery()
	view = session.query(Victims).filter(Victims.city == sub).all()
	return render_template('view3.html', view3 = view)


#@app.route('/view4')
#def view4():
#	return render_template('view4.html', view4 = view)


# Returns fname, lname, crashno, gender, dob, city from the victims table if they are female OR if their crash city is the same as their home city
@app.route('/view5')
def view5():
	sub = session.query(Crashes.crashcity).filter(Crashes.crashcity == Victims.city).subquery()
	qry1 = session.query(Victims).add_columns(Victims.fname, Victims.lname, Victims.crashno, Victims.dob, Victims.gender, Victims.city).filter(sub == Victims.city)
	qry2 = session.query(Victims).add_columns(Victims.fname, Victims.lname, Victims.crashno, Victims.dob, Victims.gender, Victims.city).filter(Victims.gender == 'F')
	view = qry1.union(qry2)
	return render_template('view5.html', view5 = view)


# Returns fname, lname, crashno, victimid, and location of those who were involved in accidents that occurred in the morning
@app.route('/view6')
def view6():
	view = session.query(Victims, Crashes).add_columns(Victims.fname, Victims.lname, Crashes.crashno, Victims.victimid, Crashes.location).filter(Crashes.crashno == Victims.crashno, Crashes.crashtime == 'Morning').all()
	return render_template('view6.html', view6 = view)


#Returns all columns in victim table where the victimid matches the victimid in the vehicles table where the make is Toyota
@app.route('/view7')
def view7():
	view = session.query(Victims).filter(Vehicles.vehicleid == Victims.vehicleid, Vehicles.make == 'Toyota').all()
	return render_template('view7.html', view7 = view)


# Returns the lplate, make, model, fname and lname of every victim
@app.route('/view8')
def view8():
	view = session.query(Vehicles, Victims).add_columns(Vehicles.lplate, Vehicles.make, Vehicles.model, Victims.fname, Victims.lname).filter(Vehicles.vehicleid == Victims.vehicleid).all()
	return render_template('view8.html', view8 = view)


# Returns victimid, fname, lname of victims and make, model of vehicles where the crash occured at night
@app.route('/view9')
def view9():
	view = session.query(Victims, Vehicles, Crashes).add_columns(Victims.vehicleid, Victims.fname, Victims.lname, Vehicles.make, Vehicles.model).filter(Crashes.crashno == Victims.crashno, Victims.vehicleid == Vehicles.vehicleid, Crashes.crashtime == 'Night').all()
	return render_template('view9.html', view9 = view)


# Returns victimid, fname, lname of victims as well as the make and model of their vehicles, and if the victim suffered a fatality where a back injury occured to the victim
@app.route('/view10')
def view10():
	view = session.query(Victims, Vehicles, Injuries).add_columns(Victims.victimid, Victims.fname, Victims.lname, Vehicles.make, Vehicles.model, Injuries.fatality).filter(Injuries.crashno == Victims.crashno, Vehicles.vehicleid == Victims.vehicleid, Injuries.injurytype == 'Back').all()
	return render_template('view10.html', view10 = view)


# create simple api that takes in crashnumber and response with crash details of said crash
# http://localhost:5000/api/2003
@app.route('/api/<crashnumber>')
def crashesJSON(crashnumber):
	crashes = session.query(Crashes).filter_by(crashno = crashnumber).one()
	return jsonify(crashes = crashes.serialize)
	

# start webserver on port 5000
# http://localhost:5000/
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)