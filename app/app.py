# Check if today is december 25th if it is say Happy Holidays
# If it is not December 25th say have a nice day

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    if now.month == 12 and now.day == 25:
        return "Happy Holidays!"
    else:
        return "Have a nice day!"