from flask import Flask,jsonify
import requests


x = requests.get('https://github.com/lokichowdary/flask_programs/blob/master/file1.log')

print(jsonify(x))




