from flask import Flask, render_template, url_for, redirect
import re
import random
import html
import os
import sys
import numpy as np
import random as r


app = Flask(__name__)

def choose_random_index(weights):
    rand = r.uniform(0, 1)
    t = 0
    sum = weights[0]
    while rand > sum:
        t += 1
        sum = sum + weights[t]
    return min(t, len(weights)-1)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/output/<string:data>')
def word(data):
    try:
        name = ''
        DATA = re.split('(\D+)', data)[1:]

        number_of_people = int(len(DATA)/2)

        NAMES = [''] * number_of_people
        NUMBERS = np.zeros(number_of_people)

        for i in range(number_of_people):
            NAMES[i] = DATA[2*i]
            NUMBERS[i] = DATA[2*i+1]

        name = NAMES[choose_random_index(NUMBERS/sum(NUMBERS))]
    except:
        error = sys.exc_info()[1]
        return render_template('output.html', name=name, error='Make sure you'
        + ' have entered alternating words or phrases, and numbers, and a ' +
        'number after every phrase.')
    return render_template('output.html', name=name, error='')




if __name__ == "__main__":
    app.run(port=5002)
