from flask import Flask , jsonify , Response
import requests
import json

app = Flask(__name__)

@app.route('/')
def check1():
    url = 'https://github.com/lokichowdary/flask_programs'
    response = requests.get(url)
    print(response.json())
    return str(response.text)


    
if __name__ == '__main__':
   app.run(debug = True)   