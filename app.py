from flask import Flask
from instagramAPI import extract_data

app = Flask(__name__)

@app.route('/<url>', methods=['GET'])
def hello(url):
    likes, features = extract_data(post_url=url)
    print(likes)
    print(features)
    return {'total': likes, "likes": features}

@app.route('/', methods=['GET'])
def home():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, port=5003)
