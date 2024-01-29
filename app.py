from flask import Flask, request, jsonify
from instagramAPI import extract_data
import requests, json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/', methods=['POST'])
def home():
    # Get the post url from the request and extract the post users 
    post_url = request.get_json()
    likes, users_interface, users_ml = extract_data(post_url=post_url)
    print(likes, users_interface, users_ml)
    # Url to which send the extracted users to make the predictions
    url = 'https://mlpred.azurewebsites.net/pred'
    data = requests.post(url, json=users_ml, headers={'Content-Type': 'application/json'})
    data = json.loads(data.content)
    # Count the humans and bots after the prediction 
    bot_count = 0
    human_count = 0
    for item in data:
        if item['prediction'] == 'bot':
            bot_count += 1
        elif item['prediction'] == 'human':
            human_count += 1
    for index, user in enumerate(users_interface):
        user.update(data[index])
    users = []
    # Match the results of the prediction with some features
    for element in users_interface:
        users.append([element['profile_image_url'], element['screen_name'], element['verified'], element['prediction'], element['probability']])
    # Send the response  
    return jsonify(human_count, bot_count, likes, users)

# For testing purposes
@app.route('/test', methods=['GET'])
def test():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
