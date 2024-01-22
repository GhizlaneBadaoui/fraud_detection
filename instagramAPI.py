import requests
import itertools
import config
import re

columns_to_include = ['id', 'screen_name', 'verified', 'followers_count', 'friends_count', 'description',
                      'profile_image_url']

def extract_shortcode(url):
    match = re.search(r'/p/([^/]+)/', url)

    if match:
        shortcode = match.group(1)
        return shortcode
    else:
        return url


"""
    Function to get 40 likers of a post and total number of likes
    API used : IG Data API with 25 requests per mounth
    :param url: url of the post
"""
def get_post_likers(url):
    querystring = {"post": url}
    headers = {
        "X-RapidAPI-Key": config.api_key,
        "X-RapidAPI-Host": "instagram-data1.p.rapidapi.com"
    }
    response = requests.get(config.api_url_2, headers=headers, params=querystring)
    return {'likes_count': response.json()['count'], 'likes': response.json()['collector']}


"""
    Function to get user information
    API used : Instagram Scraper 2023 API with 50 requests per mounth
    :param username: username of the user
"""
def get_user_info_1(username):
    headers = {
        "X-RapidAPI-Key": config.api_key,
        "X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
    }
    response = requests.get(config.api_url_3 + username, headers=headers)
    # print(response.content)
    if 'data' in response.json():
        return response.json()['data']
    return None

def get_post_likers_2(url):
    print(url)
    url = config.api_url_4 + extract_shortcode(url) + "/4/%7Bend_cursor%7D"
    headers = {
        "X-RapidAPI-Key": config.api_key,
        "X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    # print(response.content)
    return {'likes_count': response.json()['data']['count'], 'likes': response.json()['data']['likes']}

"""
    Function to get user information
    API used : IG API with 10 requests per day
    :param username: username of the user
"""
def get_user_info_2(username):
    querystring = {"user_name": username}
    headers = {
        "X-RapidAPI-Key": config.api_key,
        "X-RapidAPI-Host": "instagram28.p.rapidapi.com"
    }
    response = requests.get(config.api_url_1, headers=headers, params=querystring)
    # print(response.json())
    if 'data' in response.json():
        return response.json()['data']
    return None


# ################################## MAIN ############################################
def extract_data(post_url):
    users = []
    response = get_post_likers_2(post_url)

    for user in itertools.islice(response['likes'], 2):
        print(user['username'])
        result = get_user_info_1(user['username'])
        if result:
            user_data = {
                'id': result.get('id'),
                'screen_name': result.get('username'),
                'verified': result.get('is_verified'),
                'followers_count': (result.get('edge_followed_by')).get('count'),
                'friends_count': (result.get('edge_follow')).get('count'),
                'description': 1 if result.get('biography') else 0,
                'profile_image_url': 1 if result.get('profile_pic_url') else 0
            }
            users.append(user_data)
            # print(user_data)

    for user in itertools.islice(response['likes'], 2, 4):
        print(user['username'])
        result = get_user_info_2(user['username'])
        if result:
            user_data = {
                'id': (result.get('user')).get('id'),
                'screen_name': (result.get('user')).get('username'),
                'verified': (result.get('user')).get('is_verified'),
                'followers_count': ((result.get('user')).get('edge_followed_by')).get('count'),
                'friends_count': ((result.get('user')).get('edge_follow')).get('count'),
                'description': 1 if (result.get('user')).get('biography') else 0,
                'profile_image_url': 1 if (result.get('user')).get('profile_pic_url') else 0
            }
            users.append(user_data)
            # print(user_data)
    return response['likes_count'], users


