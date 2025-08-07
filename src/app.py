from flask import Flask, render_template
from addition import add

app = Flask(__name__)

@app.route("/")
def index():
    result = add(5, 7)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
