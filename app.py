__author__ = 'James Polera'
__email__  = 'james@uncryptic.com'
__since__  = '2011-09-14'

from flask import Flask, request
app = Flask(__name__)
from core import Receiver, Handler

@app.route("/", methods=['GET'])
def index():
    r = Receiver()
    return r.pickup("/echo","POST")

@app.route("/echo", methods=['POST'])
def echo():
    dtmf = request.form['Digits']
    h = Handler(dtmf)
    return h.read_back()

if __name__ == "__main__":
    app.debug=True
    app.run()
