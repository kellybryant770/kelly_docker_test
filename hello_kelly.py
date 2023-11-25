from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_kelly():
    return '<html><body><h1>Hello, Kelly, way to go dude today!</h1></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)