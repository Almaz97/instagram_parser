from flask import Flask, send_file, send_from_directory
from instaparser.agents import AgentAccount
import json
import os

app = Flask(__name__)
TOTAL = None
username = os.environ.get('INSTAGRAM_USERNAME')
password = os.environ.get('INSTAGRAM_PASSWORD')
account = AgentAccount(username, password)
file_path = os.environ.get("FILE_PATH")
file_name = os.environ.get("FILE_NAME")

def getFollowers():
    global TOTAL
    account.update(account)

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

    return foll_dict


@app.route('/')
def index():

    foll_dict = getFollowers()

    return json.dumps(foll_dict) # Return serialized python dictionary to json


@app.route('/return-gifs')
def return_file():
    return send_from_directory(file_path, file_name, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
