from flask import Flask, send_from_directory
# from flask_cors import CORS #comment this on deployment

app = Flask(__name__)

# serve from public 
app = Flask(__name__, static_url_path='', static_folder='frontend/public')

# CORS(app) #comment this on deployment


# @app.route("/")
# def index():
#     print(__name__)
#     return '<h1>hello this is the new version!'

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')
