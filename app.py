from flask import Flask, request
import requests
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    remote_file_url = "http://127.0.0.1:5000/getModel"
    local_file_path = "trained_model.joblib"

    try:
        # Download the remote file and save it locally
        response = requests.get(remote_file_url)

        if response.status_code == 200:
            with open(local_file_path, 'wb') as local_file:
                local_file.write(response.content)
            model_filename = 'trained_model.joblib'
            loaded_model = joblib.load(model_filename)
            return loaded_model.test
        else:
            return(f"Failed to download remote file. HTTP Status Code: {response.status_code}")
    except Exception as e:
        return(f"An error occurred: {e}")

@app.route('/test')
def text():
    url = "http://127.0.0.1:5000/test"
    response = requests.get(url)
    return response.content
    

if __name__ == '__main__':
    app.run(debug=True, port=5002)