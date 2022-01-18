import json
import emoji
import re

file = open('greek_emvolio_tweets_filtered_combined.json', 'r', encoding='utf-8')
data = file.read()
file.close()

tweets_dataset = json.loads(data)

text_data = [tweet['text'] for tweet in tweets_dataset]

# handling emojis
demojized_text = [emoji.demojize(text) for text in text_data]
#print(demojized_text)

# replacing URLs with string
no_urls_text = [re.sub(r"http[s]?:[a-zA-Z0-9_.+-/#~]+", r'<url>', demojized_tweet, flags=re.MULTILINE)for demojized_tweet in demojized_text]

print(no_urls_text)

no_users_text = [re.sub(r'@\S+', r'<user>', demojized_tweet, flags=re.MULTILINE)for demojized_tweet in no_urls_text]

mid_index = len(no_users_text)//2

vaita_data = no_users_text[:mid_index]
vasileia_data = no_users_text[mid_index:]

with open('vaita_data.txt', 'w', encoding='utf-8') as f:
    for item in vaita_data:
        f.write("%s\n" % json.dumps(item, ensure_ascii=False))
f.close()

with open('vasileia_data.txt', 'w', encoding='utf-8') as f:
    for item in vasileia_data:
        f.write("%s\n" % json.dumps(item, ensure_ascii=False))
f.close()
