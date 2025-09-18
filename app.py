from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("final_model.pkl")
scaler = joblib.load("scaler_obj.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        values = [float(x) for x in request.form.values()]
        features = np.array(values).reshape(1, -1)
        features = scaler.transform(features)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0, 1]

        result = "Malignant (Cancerous)" if prediction == 1 else "Benign (Non-Cancerous)"
        return render_template("index.html",
                               prediction_text=f"Prediction: {result}",
                               probability_text=f"Probability of Malignant: {probability:.2f}")
    except Exception as e:
        return render_template("index.html",
                               prediction_text="Error in prediction",
                               probability_text=str(e))

if __name__ == "__main__":
    app.run(debug=True)