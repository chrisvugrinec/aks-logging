from flask import Flask
from flask import Flask, render_template
from redis import Redis
import os
import socket
import logging
import sys


app = Flask(__name__)
redis = Redis(host='redis', port=6379)
#logging.basicConfig(filename='/var/log/containers/webcounter.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)

@app.route('/')
def pagecounter():
    count = redis.incr('hits')
    return render_template('index.html', counter=count);

@app.route('/arryn')
def arryn():
    count = redis.incr('hit-arryn')
    logging.info('Somebody liked the arryns, counter '+str(count))
    return render_template('index.html', arryncounter=count);

@app.route('/stark')
def stark():
    count = redis.incr('hit-stark')
    logging.info('Somebody liked the starks, counter '+str(count))
    return render_template('index.html', starkcounter=count);

@app.route('/barratheon')
def barratheon():
    count = redis.incr('hit-barratheon')
    logging.info('Somebody liked the Barratheons, counter '+str(count))
    return render_template('index.html', barratheoncounter=count);

@app.route('/dorne')
def dorne():
    count = redis.incr('hit-dorne')
    logging.info('Somebody liked the Dornes,counter '+str(count))
    return render_template('index.html', dornecounter=count);

@app.route('/greyjoy')
def greyjoy():
    count = redis.incr('hit-greyjoy')
    logging.info('Somebody liked the Greyjoys, counter '+str(count))
    return render_template('index.html', greyjoycounter=count);

@app.route('/lannister')
def lannister():
    count = redis.incr('hit-lannister')
    logging.info('Somebody liked the Lanisters, counter '+str(count))
    return render_template('index.html', lannistercounter=count);

@app.route('/targaryan')
def targaryan():
    count = redis.incr('hit-targaryan')
    logging.info('Somebody liked the Targaryans, counter '+str(count))
    return render_template('index.html', targaryancounter=count);

@app.route('/tully')
def tully():
    count = redis.incr('hit-tully')
    logging.info('Somebody liked the Tullys, counter '+str(count))
    return render_template('index.html', tullycounter=count);

@app.route('/tyrell')
def tyrell():
    count = redis.incr('hit-tyrell')
    logging.info('Somebody liked the Tyrells, counter '+str(count))
    return render_template('index.html', tyrellcounter=count);

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
