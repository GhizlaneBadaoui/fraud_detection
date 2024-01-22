from flask import Flask, request, send_file
from instagramAPI import extract_data
import requests

app = Flask(__name__)

@app.route('/<url>', methods=['GET'])
def hello(url):
    likes, features = extract_data(post_url='https://www.instagram.com/insatoulouse/p/C2KGUkQNfqs/?hl=fr')
    print(likes)
    print(features)
    return url
    
@app.route('/', methods=['GET'])
def home():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True, port=5003)