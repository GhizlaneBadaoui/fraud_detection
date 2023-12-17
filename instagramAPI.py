import requests
import csv
import itertools
import config
import sys

columns_to_include = ['id', 'screen_name', 'verified', 'followers_count', 'friends_count', 'description',
                      'profile_image_url']

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
    if 'data' in response.json():
        return response.json()['data']
    return None


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
    response = get_post_likers(post_url)

    with open(config.likes_file_path, 'w', newline='', encoding="utf8") as output_file:
        for index, user in enumerate(response['likes']):
            if index == 0:
                csv_writer = csv.DictWriter(output_file, fieldnames=user.keys())
                csv_writer.writeheader()
            csv_writer.writerow(user)

    with open(config.output_file_path, 'w', newline='', encoding="utf8") as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=columns_to_include)
        csv_writer.writeheader()

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
                csv_writer.writerow(user_data)
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
                csv_writer.writerow(user_data)
                # print(user_data)
    return response['likes_count']


if __name__ == "__main__":
    post_url = sys.argv[-1]
    likes = extract_data(post_url=post_url)
    print("Number of likes :", likes)
