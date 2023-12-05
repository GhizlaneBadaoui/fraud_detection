import csv

file_path = 'twitter_human_bots_dataset.csv'
output_file_path = 'selected_data.csv'
columns_to_include = ['id', 'followers_count', 'friends_count', 'verified', 'average_tweets_per_day', 'account_age_days', 'account_type']

with open(file_path, encoding="utf8") as file, open(output_file_path, 'w', newline='', encoding="utf8") as output_file:
    csv_reader = csv.DictReader(file)

    csv_writer = csv.DictWriter(output_file, fieldnames=columns_to_include)
    csv_writer.writeheader()

    liste = []
    header = next(csv_reader)
    for label in header:
        liste.append(label)

    #print(liste)

    for row in csv_reader:
        selected_data = {column: row[column] for column in columns_to_include}
        csv_writer.writerow(selected_data)

        # print({'id': row[liste[0]],
        #        'followers_count': row['followers_count'],
        #        'friends_count': row['friends_count'],
        #        'verified': row['verified'],
        #        'average_tweets_per_day': row['average_tweets_per_day'],
        #        'account_age_days': row['account_age_days'],
        #        'account_type': row['account_type']
        #        })


