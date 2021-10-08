# import packages
# sql packages
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

# datetime packages
from datetime import datetime as dt
from datetime import timedelta


# create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect
Base = automap_base()
Base.prepare(engine, reflect = True)


# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# create connection
# conn = engine.connect()

# # Create session
# session = Session(engine)

# # create app
# app = Flask(__name__)

# # define homepage route. This will list all the routes
# @app.route("/")
# def homepage():
#     # create variables for all routes
#     home = "/"
#     precipitation = "/api/v1.0/precipitation"
#     stations = "/api/v1.0/stations"
#     tobs = "/api/v1.0/tobs"
#     start = "/api/v1.0/<start>"
#     temps = "/api/v1.0/<start> and /api/v1.0/2011-01-01/2011-01-016"

#     return f""" Welcome to the Weather Info API! <br> 
#                 <br> To access these routes please copy and paste them into your browser <br> 
#                 The avaible routes are as follow: <br> <br>
#                 Home page: {home} <br>
#                 Preciptitation Info: {precipitation} <br>
#                 Station Info: {stations} <br>
#                 Tobs Info: {tobs} <br>
#                 From data Info : {start} <br>
#                 Temps Info: {temps}"""

# # precipation page done
# @app.route("/api/v1.0/precipitation")
# def precipation():
#     # find the date of 12 months before the last day of the data set
#     last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
#     last_date = dt.strptime(str(last_date[0]),"%Y-%m-%d").date()
#     year_ago = last_date - timedelta(days = 365)

#     # query the prcp values from the last 12 months
#     last_year = session.query(measurement.date,measurement.prcp).filter(measurement.date >= year_ago).all()

#     prcp_list = []
#     # store values in a dictionary
#     for date in last_year:
#         # create empty dictionary at each iteration
#         prcp_dict = {}

#         # add date value to Date key in dict
#         prcp_dict["Date"] = date.date

#         # add prcp value to prcp  key in dict
#         prcp_dict["prcp"] = date.prcp
#         prcp_list.append(prcp_dict)

#     return jsonify(prcp_list)

# # stations page
# @app.route("/api/v1.0/stations")
# def stations():
#     stations = session.query(station.station)
#     station_dict = {}
#     for s in stations:
#         station_dict["station"] = s
#     return jsonify(station_dict)

# # Define main
# if __name__ == "__main__":
#     app.run(debug =True)