from flask import Flask, request
from main import FraudDetectionModel
app = Flask(__name__)


model = FraudDetectionModel("clean_data.csv")

@app.route('/', methods=['GET', 'POST'])
def hello():
    return model.init()

@app.route('/prediction')
def predict():
    return model.predict_with_confidence()

if __name__ == '__main__':
    app.run(debug=True)