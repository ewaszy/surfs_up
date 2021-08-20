# Import the Flask dependency
from flask import Flask

#  Create a new Flask instance called app
app = Flask(__name__)

## Create Flask Routes
# Define the starting point
@app.route('/')
def hello_world():
    return'Hello world'

# Run a Flask App - On Windows 
# Enter set FLASK_APP=app.py in Anaconda Powershell