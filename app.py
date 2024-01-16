from flask import Flask, request, send_file
from main import FraudDetectionModel
import joblib

app = Flask(__name__)


model = FraudDetectionModel("clean_data.csv")

@app.route('/', methods=['GET'])
def hello():
    model.init()
    model_filename = 'saved_model.joblib'
    joblib.dump(model, model_filename)
    return send_file(model_filename, as_attachment=True)

@app.route('/test')
def test():
    return "hello2"


if __name__ == '__main__':
    app.run(debug=True)