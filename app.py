from flask import Flask

app = Flask(__name__)

# serve from public 

@app.route("/")
def index():
    print(__name__)
    return '<h1>hello this is the new version!</h1><div>ligma</div>'

