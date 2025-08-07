from flask import Flask
from addition import add

app = Flask(__name__)

@app.route("/")
def index():
    result = add(5, 7)
    return f"✅ The sum of 5 and 7 is: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
