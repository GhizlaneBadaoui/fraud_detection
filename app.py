from flask import Flask, request, jsonify
from instagramAPI import extract_data
import requests, json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/', methods=['POST'])
def hello():
    post_url = request.get_json()
    print("url ",post_url)
    likes, users_interface, users_ml = extract_data(post_url=post_url)
    print(likes, users_interface, users_ml)
    url = 'https://mlpred.azurewebsites.net/pred'
    print("******************************************")
    data = requests.post(url, json=users_ml, headers={'Content-Type': 'application/json'})
    data = json.loads(data.content)
    bot_count = 0
    human_count = 0
    print("from ..................", data)
    # Iterate through the list and count occurrences
    for item in data:
        if item['prediction'] == 'bot':
            bot_count += 1
        elif item['prediction'] == 'human':
            human_count += 1
    for index, user in enumerate(users_interface):
        user.update(data[index])
    users = []
    for element in users_interface:
        users.append([element['profile_image_url'], element['screen_name'], element['verified'], element['prediction'], element['probability']])
    
    return jsonify(human_count, bot_count, likes, users)

@app.route('/hello', methods=['GET'])
def home():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
