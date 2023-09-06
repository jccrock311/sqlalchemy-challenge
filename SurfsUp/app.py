# Import the dependencies.

from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import numpy as np
import datetime as dt

#################################################
# Database Setup
#################################################

# create engine
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)
#Base.prepare(engine, reflect=True)

# Save references to each table
measurement=Base.classes.measurement
station=Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    
    return (f"<h1> <b> The Hawaiian Climate App <b/></h1>"
            F"<br/>"
            f"<ol>"
            f"<strong><h2> Routes: </h2></strong><br/>"
            f"<li><h3>/api/v1.0/precipiation </h3><br/>"
            f"<li><h3>/api/v1.0/stations </h3><br/>"
            f"<li><h3>/api/v1.0/tobs </h3><br/>"
            f"<li><h3>/api/v1.0/temp/start</h3><br/>"
            f"<li><h3>/api/v1.0/temp/start/end</h3><br/>"
            f"<ol>"
            )
    
# Precipitation analysis:
@app.route("/api/v1.0/precipiation")
def precipitaion():
   
    
# List of stations  
@app.route("/api/v1.0/stations")
def stations():
    
# Most active stations
@app.route("/api/v1.0/tobs")
def active_stations():
    
# Return min, max, and avg for a specified start or start-end range 
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def start_end_temps(start=None, end=None):