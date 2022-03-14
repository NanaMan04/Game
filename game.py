import random
import operator
import itertools
import math
from statistics import mode
from flask import Flask, render_template


l = []
op = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
for i in range(5):
    l.append(random.randint(1,50))
y = []
for i in itertools.product(op, repeat=4):
    y.append(i)
g = []
for i in itertools.permutations(l):
    g.append(i)
t = []
for i in g:
    for j in y:
        t.append(j[3][1](j[2][1](j[1][1](j[0][1](i[0], i[1]), i[2]), i[3]), i[4]))

app = Flask(__name__)



        