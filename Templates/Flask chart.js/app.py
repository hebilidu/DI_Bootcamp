from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    data = [
        ("2020-01-01", 1597),
        ("2020-01-02", 1456),
        ("2020-01-03", 1908),
        ("2020-01-04", 896),
        ("2020-01-05", 755),
        ("2020-01-06", 453),
        ("2020-01-07", 1100),
        ("2020-01-08", 1235),
        ("2020-01-09", 1478),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("graph.html", labels=labels, values=values)
