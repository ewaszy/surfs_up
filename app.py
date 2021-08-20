# Import the Flask dependency
from flask import Flask

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