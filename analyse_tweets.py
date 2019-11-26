import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv('tweets.csv')

#unique_users = list(set(data['User ID']))

retweets = data.loc[data['Retweeted ID'].isin(data['Tweet ID'])]
retweeteds = data.loc[data['Tweet ID'].isin(retweets['Retweeted ID'])]

unique_retweeters = list(set(retweets['User ID']))


dict_of_lists = {}
for retweeter in unique_retweeters:
    retweet_data = retweets[retweets['User ID'] == retweeter]
    retweeted_data = retweeteds[retweeteds['Tweet ID'].isin(retweet_data['Retweeted ID'])]
    retweeted_users = list(set(retweeted_data['User ID']))
    for user in retweeted_users:
        if user in dict_of_lists.keys():
            dict_of_lists[user].append(retweeter)
        else:
            dict_of_lists[user] = [retweeter]

graph_dict = dict_of_lists.copy()

for key in dict_of_lists.keys():
    if len(dict_of_lists[key]) <= 10:
        del graph_dict[key]

graph = nx.Graph(graph_dict)
nx.draw(graph)
plt.savefig("graph.png")
plt.show()