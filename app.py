import os
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model with path relative to this script
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "student_score_model.pkl")

if not os.path.exists(model_path):
    print(f"Error: Model file not found at {model_path}")
    exit(1)

model = joblib.load(model_path)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    range_avg = None
    range_above = None

    if request.method == "POST":
        try:
            hours = float(request.form["hours"])
            attendance = float(request.form["attendance"])
            prev_score = float(request.form["prev_score"])
            sleep = float(request.form["sleep"])
            features = np.array([[hours, attendance, prev_score, sleep]])
            pred = model.predict(features)[0]

            mae = 1.41  # your MAE
            prediction = round(pred, 2)
            range_avg = (round(pred - mae, 1), round(pred + mae, 1))
            range_above = (round(pred - mae, 1), round(pred + 8 * mae, 1))
        except (ValueError, KeyError):
            pass

    return render_template("index.html",
                           prediction=prediction,
                           range_avg=range_avg,
                           range_above=range_above)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
