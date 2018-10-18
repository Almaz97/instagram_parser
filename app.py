from flask import Flask
from instaparser.agents import AgentAccount
import json
import os

app = Flask(__name__)


def getFollowers(username, password):

    account = AgentAccount(username, password)
    amt_of_followers = account.followers_count

    with open('amount.txt', 'r') as amount:
        if os.stat("amount.txt").st_size != 0:
            total = int(amount.read())
        else:
            total = amt_of_followers

    with open('amount.txt', 'w') as amount:
        amount.write(str(amt_of_followers))

    foll_dict = dict()
    foll_dict['profile'] = username
    foll_dict['number'] = amt_of_followers

    if amt_of_followers > total:
        diff = amt_of_followers - total
        get_new_followers = account.get_followers(account=account, count=diff)
        new_followers = [str(item) for item in get_new_followers[0]]
        foll_dict['followed_by'] = new_followers

    return foll_dict


@app.route('/')
def index():

    username = 'yourusername'
    password = 'yourpassword'

    foll_dict = getFollowers(username, password)

    return json.dumps(foll_dict) # Return serialized python dictionary to json


if __name__ == '__main__':
    app.run(debug=True)
