from slack import WebClient
from slackeventsapi import SlackEventAdapter
import certifi
import json

# check slack connection initially
def slack_connection(app):
    with open("secret.json", "r") as f:
        token = json.load(f)
        
    # slack_event_adapter = SlackEventAdapter(token['slack_signing_secret'], "/slack/events", app)
    # initialize a web API client for Slack
    slack_client = WebClient(token=token['slack_bot_token'])

    # tester code to check if python (no Flask) and slack connected
    # response = slack_client.chat_postMessage(channel='#random', text="Hello, world!")
    # assert response["ok"]
    # assert response["message"]["text"] == "Hello, world!"



# if __name__=="__main__":
#     slack_connection()