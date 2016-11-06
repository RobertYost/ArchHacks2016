import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import serial

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

started = False

@ask.launch
def new_start():
    msg = render_template('introduction')
    return question(msg)

@ask.intent("YesIntent")
def next_round():
    global started
    if started:
        msg = render_template('fall_true')
        return statement(msg)
    started = True
    ser = serial.Serial('COM4', 9600, timeout=0.1)
    while True:
        line = ser.readline()
        if len(line) > 0 and "fall" in line:
            break
    msg = render_template('fall')
    return question(msg)

@ask.intent("FallIntent")
def fall():
    global started
    if started:
        msg = render_template('fall_true')
        return statement(msg)
    started = True
    ser = serial.Serial('COM4', 9600, timeout=0.1)
    while True:
        line = ser.readline()
        if len(line) > 0 and "fall" in line:
            break
    msg = render_template('fall')
    return question(msg)

@ask.intent("NoFallIntent")
def nofall():
    global started
    if started:
        msg = render_template('fall_false')
        return statement(msg)
    msg = render_template('repeat')
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)