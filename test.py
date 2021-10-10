# import packages
# sql packages
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, session
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
conn = engine.connect()

# # Create session
session = Session(engine)

session.query(station.station).all()