from flask import Flask, render_template, request
import joblib
import sklearn
import pandas as pd


# Sanity check (optional but useful)
print("scikit-learn version:", sklearn.__version__)

app = Flask(__name__)

# Load trained objects
pipeline = joblib.load("model/student_pipeline.pkl")
features = joblib.load("model/feature_order.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect input values
        input_data = [request.form[f] for f in features]

        # Convert to DataFrame (THIS IS THE KEY FIX)
        input_df = pd.DataFrame([input_data], columns=features)

        # Predict
        pred_encoded = pipeline.predict(input_df)[0]
        prediction = label_encoder.inverse_transform([pred_encoded])[0]

        return render_template(
            "index.html",
            prediction=prediction
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}"
        )



if __name__ == "__main__":
    app.run(debug=True)
