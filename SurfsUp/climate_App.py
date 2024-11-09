#Import dependencies

import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(autoload_with=engine)

# Save database references to a table
Station = Base.classes.station
Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes"""
    return(
        f"Available API Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"  
        )

# app routing for precip for the past 12 months
@app.route("/api/v1.0/precipitation")
def precipitation():

    # Create session link
    session = Session(engine)
    
    # Query the last 12 months of precip data
    recent_date = '2016-08-23'
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= recent_date ).all()
    session.close()

    # Create a dictionary from the results and append to a list of precipitation_data
    precip_data = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip_data.append(precip_dict)
    return jsonify(precip_data)

 #app routing for station list
@app.route("/api/v1.0/stations")
def stations():

    # Create session link
    session = Session(engine)
    
    # Query the names of all stations in the list
    results = session.query(Station.station).distinct().all()
    session.close()

    # Create a dictionary of the active stations and their counts
    station_data = []
    for station in results:
        station_dict = {}
        station_dict["station name"] = station[0]
        station_data.append(station_dict)
    return jsonify(station_data)

#app routing for t_observed for the past 12 months
@app.route("/api/v1.0/tobs")
def tobs():
    recent_date = '2016-08-23'

    # Create session link
    session = Session(engine)

    # Query the last 12 months of temperature data from the most active observation station 
  
    results = session.query(Measurement.date, Measurement.tobs).filter((Measurement.station == 'USC00519281') & (Measurement.date >= recent_date)).all()
    session.close()

    # Create a dictionary of t_obs data for the most active station
    tobs_data = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Oberved Temperature"] = tobs
        tobs_data.append(tobs_dict)
    return jsonify(tobs_data)

#app routing for min, avg, max temp for a given start date
@app.route("/api/v1.0/start")
def  temps_start():
    start = '2016-06-26'

    # Create session link
    session = Session(engine)

    # Query specific start date of temperature data for  min, avg, max temp for a given start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

    # Create a dictionary of  min, avg, max temp for a given start date 
    temp_data = []
    for tobs in results:
        temp_dict = {}
        temp_dict["Minimum"] = results[0][0]
        temp_dict["Average"] = results[0][1]
        temp_dict["Maximum"] = results[0][2]
        temp_data.append(temp_dict)

    return jsonify(temp_data)

#app routing for  min, avg, max temp for a given start date and end date
@app.route("/api/v1.0/start/end")
def temps_start_end():
    start = '2016-06-26'
    end = '2016-07-26'

    # Create session link
    session = Session(engine)

    # Query specific start date of temperature data for  min, avg, max temp for a given start date and end date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter((Measurement.date >= start) & (Measurement.date <= end)).all()

    # Create a dictionary of  min, avg, max temp for a given start date and end date
    date_range_temp_data = []
    for tobs in results:
        temp_dict = {}
        temp_dict["minimum"] = results[0][0]
        temp_dict["Average"] = results[0][1]
        temp_dict["Maximum"] = results[0][2]
        date_range_temp_data.append(temp_dict)

    return jsonify(date_range_temp_data)

if __name__ == '__main__':
    app.run(debug=True)