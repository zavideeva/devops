"""
Running flask application, that shows curent time in Moskow
"""
from datetime import datetime
from flask import Flask 
import pytz

app = Flask(__name__)
MSK = pytz.timezone('Europe/Moscow')


@app.route("/")
def time_in_msk():
    """Show current time in Moskow"""
    return datetime.now(MSK).strftime('%H:%M:%S'), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
