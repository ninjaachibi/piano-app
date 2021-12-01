from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print(__name__)
    return '<h1>"Hello World!"</h1><div>ligma</div>'

