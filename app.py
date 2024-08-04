from flask import Flask
app = Flask(__name__)
from flask import request, render_template

import google.generativeai as palm
import os

api = os.getenv("MAKERSTUITE_API_TOKEN")
palm.configure(api_key=api)

model = { 'model': "models/chat-bison-001"}

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/prediction", methods = ["GET", "POST"])
def prediction():
    num = float(request.form.get("rates"))
    return(render_template("prediction.html", r = 90.2-(50.6*num)))

@app.route("/genAI", methods = ["GET", "POST"])
def genAI():
    return render_template("genAI.html")

@app.route("/genAI_reply", methods = ["GET", "POST"])
def genAI_reply():
    q = request.form.get("q")
    print("in makersuite")
    r = palm.chat(
        **model,
        messages=q
    )
    print("done makersuite")
    return render_template("genAI_reply.html",r=r.last)

if __name__=="__main__":
    app.run()
