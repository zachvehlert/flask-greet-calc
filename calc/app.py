import operations as op
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args['a']
    b = request.args['b']
    return str(op.add(a,b))

@app.route('/sub')
def sub():
    a = request.args['a']
    b = request.args['b']
    return str(op.sub(a,b))

@app.route('/mult')
def mult():
    a = request.args['a']
    b = request.args['b']
    return str(op.mult(a,b))

@app.route('/div')
def div():
    a = request.args['a']
    b = request.args['b']
    return str(op.div(a,b))

@app.route('/math/<operation>')
def do_math(operation):
    a = request.args['a']
    b = request.args['b']
    math_ops = {
        'add' : op.add,
        'sub' : op.sub,
        'mult' : op.mult,
        'div' : op.div
    }
    return str(math_ops[operation](a,b))