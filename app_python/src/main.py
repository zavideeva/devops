"""
Running flask application, that shows curent time in Moskow
"""
from datetime import datetime
from flask import Flask, make_response
import pytz
import os

app = Flask(__name__)
MSK = pytz.timezone('Europe/Moscow')
FILE = "data/visits.txt"

def create_visits():
    dirname = os.path.dirname(FILE)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    if not os.path.exists(FILE):
        os.mknod(FILE)

@app.route("/")
def time_in_msk():
    """Show current time in Moskow"""
    create_visits()
    str_time = datetime.now(MSK).strftime('%H:%M:%S')
    with open(FILE, "a+") as f:
      f.write(str_time + "\n")
    return str_time, 200

@app.route("/visits")
def show_visits():
  with open(FILE, mode='r') as f:
    response = make_response(f.read(), 200)
    response.mimetype = 'text/plain'
  return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
