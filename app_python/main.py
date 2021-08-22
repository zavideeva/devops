"""
Running flask application, that shows curent time in Moskow
"""
from datetime import datetime
from flask import Flask
import pytz

APP = Flask(__name__)
MSK = pytz.timezone('Europe/Moscow')


@APP.route("/")
def time_in_msk():
    """Show current time in Moskow"""
    return 'Time in MSK: ' + datetime.now(MSK).strftime('%H:%M:%S %Y.%m.%d')


if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=True)
