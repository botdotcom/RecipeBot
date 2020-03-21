from slack import WebClient
from slackeventsapi import SlackEventAdapter
import json
"""this file contains the connection to Slack API using various keys"""

def slack_connection(app):
    with open("secret.json", "r") as f:
        token = json.load(f)
            
    # initialize a web API client for Slack
    slack_client = WebClient(token=token['slack_bot_token'])
    slack_event_adapter = SlackEventAdapter(token['slack_signing_secret'], "/slack/events", app)
    return [slack_client, slack_event_adapter]


def bot_response(slack_client, title, url, channel):
    # composed_text = "Try out this recipe:\n{} -- {}".format(title, url)
    composed_text = "Try out this recipe:\n{}".format(url)
    response = slack_client.chat_postMessage(channel=channel, text=composed_text)


# check slack connection initially
# def slack_connection():
    # tester code to check if python (no Flask) and slack connected
    # response = slack_client.chat_postMessage(channel='#random', text="Hello, world!")
    # assert response["ok"]
    # assert response["message"]["text"] == "Hello, world!"