#import libraries
from flask import Flask
from flask import request
from flask import Response
import math
import random
import string
import calc
import json

#boilerplate code to run flask app
app = Flask(__name__)
@app.route("/")

#benchmark function called during benchmarking of the application
def benchmark():

    #save the two query string parameters i1 and i2
    i1 = int(request.args.get('i1'))
    i2 = int(request.args.get('i2'))

    #call the calc.calculation function as defined in the calc.py app
    result = calc.calculation(i1, i2)

    #print the results in JSON format
    resultJSON={
        "i1" : i1,
        "i2" : i2,
        "Calculated Value" : result
    }

    #create a response message of JSON printout
    reply = json.dumps(resultJSON)

    #send response and status 200 to show successful response
    r = Response(response=reply, status=200, mimetype="application/json")
    r.headers["Content-Type"]="application/json"
    r.headers["Access-Control-Allow-Origin"]="*"
    return r

#boilerplate code to run flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
