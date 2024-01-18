from flask import Flask, request, send_file
from instagramAPI import extract_data
import requests

app = Flask(__name__)

@app.route('/<url>', methods=['GET'])
def hello(url):
    likes = extract_data(post_url=url)
    return "hello"
    
@app.route('/', methods=['GET'])
def home():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)