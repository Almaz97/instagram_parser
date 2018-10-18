from flask import Flask
from instaparser.agents import AgentAccount
import json
import os

app = Flask(__name__)
TOTAL = None


def getFollowers(username, password):
    global TOTAL

    account = AgentAccount(username, password)
    amt_of_followers = account.followers_count
    foll_dict = dict()
    foll_dict['profile'] = username
    foll_dict['number'] = amt_of_followers

    if TOTAL is None:
        TOTAL = amt_of_followers
    else:
        if amt_of_followers > TOTAL:
            diff = amt_of_followers - TOTAL
            get_new_followers = account.get_followers(account=account, count=diff)
            new_followers = [str(item) for item in get_new_followers[0]]
            foll_dict['followed_by'] = new_followers
            TOTAL = amt_of_followers
        elif amt_of_followers < TOTAL:
            TOTAL = amt_of_followers

    account.update(account)
    return foll_dict


@app.route('/')
def index():

    username = os.environ.get('INSTAGRAM_USERNAME')
    password = os.environ.get('INSTAGRAM_PASSWORD')

    foll_dict = getFollowers(username, password)

    return json.dumps(foll_dict) # Return serialized python dictionary to json


if __name__ == '__main__':
    app.run(debug=True)
