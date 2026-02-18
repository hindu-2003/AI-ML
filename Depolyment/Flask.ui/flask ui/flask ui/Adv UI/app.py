from flask import Flask, render_template, request
import numpy as np
import pickle
import sklearn

app = Flask(__name__)

print("Flask using sklearn version:", sklearn.__version__)

# Load trained model
with open("advertising_pipeline.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        try:
            tv = float(request.form["TV"])
            radio = float(request.form["radio"])
            newspaper = float(request.form["newspaper"])

            input_data = np.array([[tv, radio, newspaper]])

            pred = model.predict(input_data)[0]
            prediction = round(pred, 2)

        except Exception as e:
            prediction = "Invalid Input"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
