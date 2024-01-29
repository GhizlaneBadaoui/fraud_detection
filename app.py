from flask import Flask, request, send_file
from main import FraudDetectionModel
import joblib
import requests

app = Flask(__name__)

# Instanciate the model (not trained yet) using the dataset
model = FraudDetectionModel("clean_data.csv")

@app.route('/', methods=['GET'])
def home():
    # Train the model
    model.init()
    # The file name that contains the trained model 
    model_filename = 'saved_model.joblib'
    joblib.dump(model, model_filename)
    # Send the response
    return send_file(model_filename, as_attachment=True)

# For testing purposes
@app.route('/test')
def test():
    return "hello from the training MS"

if __name__ == '__main__':
    app.run(debug=True, port=5003)