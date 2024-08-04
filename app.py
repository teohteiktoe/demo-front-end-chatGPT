from flask import Flask
app = Flask(__name__)
from flask import request, render_template

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/prediction", methods = ["GET", "POST"])
def prediction():
    num = float(request.form.get("rates"))
    return(render_template("prediction.html", r = 90.2-(50.6*num)))

if __name__=="__main__":
    app.run()
