from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import json
import service as sv
import slackrecipebot as srb
"""this file contains the flask endpoints"""


# this is the main flask app with my endpoints
app = Flask(__name__)
# added additional URL
run_with_ngrok(app)

# Slack events adapter etc
slack_client, slack_event_adapter = srb.slack_connection(app)

# endpoints for slack
# simple slack endpoint to read message when bot is mentioned
@slack_event_adapter.on("app_mention")
def user_message(payload):
    event = payload.get("event", {})
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    message = text.split(" ")
    # for sending to slack
    url = ""
    title = ""

    if message[1] == "ingredient" or message[1] == "ingredients":
        ingredients = message[2:]
        recipes = make_recipe_by_ingredients(ingredients)
        # currently retrieving only 1 recipe
        rid = recipes[0]["id"]
        recipe = make_recipe_by_id(rid)
        url = recipe["sourceUrl"]
        # title = recipe["sourceName"]

    if message[1] == "random":
        recipe = make_random_recipe()
        url = recipe["recipes"][0]["sourceUrl"]
        # title = recipe["recipes"][0]["sourceName"]

    srb.bot_response(slack_client, title, url, channel_id)
    return render_template("home.html") #temp


# slack verifier -- used this only once, for establishing a new URL on Slack app
# @app.route('/slack/events', methods=['POST'])
# def verify_slack():
#     payload = request.json
#     return payload['challenge']


# endpoints for direct users with Spoonacular
# default page where app lands
@app.route('/recipes')
def default():
    return render_template("home.html")


# get recipes from list of ingredients
@app.route('/recipes/ingredients')
def get_recipes_by_ingredients():
    ingredients = request.args.getlist('items')
    recipes = make_recipe_by_ingredients(ingredients)   # DRY
    # print(recipes)
    return render_template("searchresults.html")


# get a random recipe
@app.route('/recipes/random')
def get_random_recipes():
    recipes = make_random_recipe()  # DRY
    print(recipes)
    return render_template("searchresults.html")


# helper methods for DRY
# pass list of ingredients to API and get recipes in return
def make_recipe_by_ingredients(ingredients):
    response = sv.recipes_by_ingredients(ingredients)
    return response.json()


# call to get a random recipe function
def make_random_recipe():
    response = sv.random_recipes()
    return response.json()


# get complete recipe information from recipe id fetched earlier
def make_recipe_by_id(recipe_id):
    response = sv.recipe_information_by_id(recipe_id)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)