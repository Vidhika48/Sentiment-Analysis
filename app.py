from flask import Flask, render_template, request
from joblib import load
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the models
rf_model = load('lr_bow.pkl')
vectorizer = load('vectorizer.pkl')

# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        processed_review = vectorizer.transform([review])
        prediction = rf_model.predict(processed_review)[0]
        sentiment = "Positive" if prediction == 1 else "Negative"
        return render_template('prediction.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
