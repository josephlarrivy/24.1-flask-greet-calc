# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return f'{a}+{b}={result}'

@app.route('/sub')
def sub_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return f'{a}-{b}={result}'

@app.route('/mult')
def mult_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return f'{a}*{b}={result}'

@app.route('/div')
def div_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return f'{a}/{b}={result}'





if __name__ == '__main__':
    app.run()
