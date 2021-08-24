# Import the Flask dependency
from flask import Flask,session,jsonify
import datetime as dt 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np

# Prepare the database file to be connected to later on
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Create our session (link) from Python to the DB
session = Session(engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#  Create a new Flask instance called app
app = Flask(__name__)

# Define the welcome route
@app.route("/")

# Add the routing information for each of the other routes
# Create a function and a return statement with f stings as a reference to all of the other routes 
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Create a new route for precipitation
@app.route("/api/v1.0/precipitation")

# Create the precipitation() function
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# Navigate to the precipitation route to see the output 
# Add api/v1.0/precipitation to end of the the URL 

# Create a new route for Stations
@app.route("/api/v1.0/stations")

# Create the stations() function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Navigate to the stations route to see the output 
# Add api/v1.0/stations to end of the the URL 

# Create a new route for temperatures
@app.route("/api/v1.0/tobs")

# Create the monthly temperatures() function:
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Create the Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create the stats() function:
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# Test the code with a specific date:
# To find the minimum, maximum, and average temperatures for June 2017
# Add /api/v1.0/temp/2017-06-01/2017-06-30 to the end of the URL - works