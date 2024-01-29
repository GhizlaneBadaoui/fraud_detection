from flask import Flask, request, jsonify
import requests
import joblib
import json
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

model = None

@app.route('/', methods=['GET'])
def hello():
    # The url used to get the trained model 
    remote_file_url = "https://mlflaskms.azurewebsites.net/"
    # the trained model name
    local_file_path = "trained_model.joblib"

    try:
        # Download the remote file and save it locally
        response = requests.get(remote_file_url)

        if response.status_code == 200:
            with open(local_file_path, 'wb') as local_file:
                local_file.write(response.content)
            model_filename = 'trained_model.joblib'
            global model
            model = joblib.load(model_filename)
            return model.test
        else:
            return(f"Failed to download remote file. HTTP Status Code: {response.status_code}")
    except Exception as e:
        return(f"An error occurred: {e}")

@app.route('/test', methods=['GET'])
def test():
    return "Message from the trained model : ",model.test

# Entry point to make the prediction
@app.route('/pred', methods=['POST'])
def pred():
    data = []
    # Get the request data
    json_data = request.get_json()
    for i in json_data:
        data.append([ int(v1) if k1 == 'id' else v1 for k1, v1 in i.items()])
    # Make the prediction using the model 
    resp = model.predict_with_confidence(data)
    print(resp)
    print(json.dumps(resp))
    # Send the response
    return json.dumps(resp)


if __name__ == '__main__':
    app.run(debug=True, port=5002)