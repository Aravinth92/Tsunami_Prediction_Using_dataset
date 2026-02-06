
from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        depth = float(request.form["depth"])
        prediction = round(model.predict(depth), 2)

    return render_template("index.html", prediction=prediction, mse=round(model.mse,3), r2=round(model.r2,3))

if __name__ == "__main__":
    app.run(debug=True)
