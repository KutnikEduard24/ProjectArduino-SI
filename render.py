from flask import Flask, render_template
import logging
import requests


# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route("/")
def form():
   # f = open("date.txt","r")
    #data = f.readline()
    with open('date.txt') as f:
        data = []
        lines = f.read()
        data = lines.split()
        for i in data:
            return render_template('index.html', variable=data[-1])

if __name__ == "__main__":
    app.run()

#USER AUTH
