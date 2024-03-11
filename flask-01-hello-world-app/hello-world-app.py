from flask import Flask 
app = Flask(__name__)

@app.route("/")
def head():
    return "Hello world Class"

@app.route("/second")
def head1():
    return "this is second page"

@app.route("/third")
def page3():
    return "this is third page"

@app.route('/<string:id>')
def forth(id):
    return f'Id of this page is {id}'

if __name__ == '__main__':

    # app.run(debug=True, port=30000)
    app.run(host= '0.0.0.0', port=8081)