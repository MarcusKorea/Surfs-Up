# import packages
# sql packages
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
<<<<<<< HEAD
from flask import Flask, json, jsonify
=======
from flask import Flask, jsonify
>>>>>>> def40436e86a9faa5d55b0c678b4ae4dc07a8230

# datetime packages
from datetime import datetime as dt
from datetime import timedelta


# create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
<<<<<<< HEAD
=======

>>>>>>> def40436e86a9faa5d55b0c678b4ae4dc07a8230
# reflect
Base = automap_base()
Base.prepare(engine, reflect = True)


# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# create connection
conn = engine.connect()

# Create session
session = Session(engine)

<<<<<<< HEAD
=======

>>>>>>> def40436e86a9faa5d55b0c678b4ae4dc07a8230
# create app
app = Flask(__name__)

# define homepage route. This will list all the routes
@app.route("/")
def homepage():
    # create variables for all routes
    home = "/"
    precipitation = "/api/v1.0/precipitation"
    stations = "/api/v1.0/stations"
    tobs = "/api/v1.0/tobs"
<<<<<<< HEAD
    start_temp = "/api/v1.0/2011-01-01"
    start_end = "/api/v1.0/2011-01-01/2011-01-16"
=======
    start = "/api/v1.0/<start>"
    temps = "/api/v1.0/<start> and /api/v1.0/2011-01-01/2011-01-016"
>>>>>>> def40436e86a9faa5d55b0c678b4ae4dc07a8230

    return f""" Welcome to the Weather Info API! <br> 
                <br> To access these routes please copy and paste them into your browser <br> 
                The avaible routes are as follow: <br> <br>
                Home page: {home} <br>
                Preciptitation Info: {precipitation} <br>
                Station Info: {stations} <br>
                Tobs Info: {tobs} <br>
<<<<<<< HEAD
                Min, Average and Max Temps from a certain Date Info: {start_temp} <br>
                Min, Average and Max Temps between Two Dates Info: {start_end}"""

# precipation page done
=======
                From data Info : {start} <br>
                Temps Info: {temps}"""

>>>>>>> def40436e86a9faa5d55b0c678b4ae4dc07a8230
@app.route("/api/v1.0/precipitation")
def precipation():
    # find the date of 12 months before the last day of the data set
    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    last_date = dt.strptime(str(last_date[0]),"%Y-%m-%d").date()
    year_ago = last_date - timedelta(days = 365)

    # query the prcp values from the last 12 months
    last_year = session.query(measurement.date,measurement.prcp).filter(measurement.date >= year_ago).all()

    prcp_list = []
    # store values in a dictionary
    for date in last_year:
        # create empty dictionary at each iteration
        prcp_dict = {}

        # add date value to Date key in dict
        prcp_dict["Date"] = date.date

        # add prcp value to prcp  key in dict
        prcp_dict["prcp"] = date.prcp
<<<<<<< HEAD

        # add values to list
=======
>>>>>>> def40436e86a9faa5d55b0c678b4ae4dc07a8230
        prcp_list.append(prcp_dict)

    return jsonify(prcp_list)

<<<<<<< HEAD
# stations page
@app.route("/api/v1.0/stations")
def stations():

    # create list of stations
    station_list = []
    
    # query the station
    stations = session.query(station.station)
     
    for s in stations:

        # create empty dictionary at each iteration
        station_dict = {}

        # add the current station to the dictionary
        station_dict["station"] = s.station

        # add the dictionary to the list of stations
        station_list.append(station_dict)

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():

    # store the count function for ease of use
    station_count = func.count(measurement.station)

    # find the latest date in the data set
    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()

    # put it in date format
    last_date = dt.strptime(str(last_date[0]),"%Y-%m-%d").date()

    # calcualte a year from the last date
    year_ago = last_date - timedelta(days = 365)


    # query station name, station station, station id and station count for the station with the most observations

    most_observed = session.query(measurement.station,station_count).group_by(measurement.station).order_by(station_count.desc()).first()[0]

    # query the station and tobs data for the most observed station
    observed_data = session.query(measurement.station, measurement.tobs,measurement.date).filter(measurement.date >= year_ago).filter(measurement.station == most_observed).all()

    tobs_list= []

    # iterate through the data
    for row in observed_data:
        tobs_dict = {}

        tobs_dict["Station"]  = row.station
        tobs_dict["tobs"] = row.tobs

        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def temp_start(start):
    # store min, max and avg functions for ease of use
    min_temp = func.min(measurement.tobs)
    max_temp = func.max(measurement.tobs)
    avg_temp = func.avg(measurement.tobs)

    # query the data from the start date
    temp = session.query(min_temp, avg_temp , max_temp).filter(measurement.date >= start).all()[0]

    # create a list for the temperatures
    temp_list = []
    
    temp_dict = {}
    temp_dict["min_temp"] = temp[0]
    temp_dict["avg_temp"] = temp[1]
    temp_dict["max_temp"] = temp[2]
        
    temp_list.append(temp_dict)

    return jsonify(temp_list)

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start,end):
    # store min, max and avg functions for ease of use
    min_temp = func.min(measurement.tobs)
    max_temp = func.max(measurement.tobs)
    avg_temp = func.avg(measurement.tobs)

    # query the data from the start date
    temp2 = session.query(min_temp, avg_temp , max_temp).filter(measurement.date >= start).filter(measurement.date <= end).all()[0]

    # create a list for the temperatures
    temp_list = []
    
    temp_dict = {}
    temp_dict["min_temp"] = temp2[0]
    temp_dict["avg_temp"] = temp2[1]
    temp_dict["max_temp"] = temp2[2]
        
    temp_list.append(temp_dict)

    return jsonify(temp_list)
=======



>>>>>>> def40436e86a9faa5d55b0c678b4ae4dc07a8230

# Define main
if __name__ == "__main__":
    app.run(debug =True)