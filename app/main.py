import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/api/v1/', methods=['POST'])
def home():
   return jsonify(request.json)


from datetime import datetime

def cronjob():
   """
   Main cron job.
   The main cronjob to be run continuously.
   """
   print("Cron job is running")
   print("Tick! The time is: %s" % datetime.now())