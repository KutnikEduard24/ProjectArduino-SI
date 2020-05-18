from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def form():
    with open('date.txt') as f:
        data = []
        lines = f.read()
        data = lines.split()
        for i in data:
            return render_template('index.html', variable=data[-1])



if __name__ == "__main__":
    app.run()
