from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import json
import service as sv
import slackrecipebot as srb

# this is the main flask app with my endpoints
app = Flask(__name__)
# added additional URL
run_with_ngrok(app)

# Slack events adapter
slack_event_adapter = srb.slack_connection(app)[1]

# endpoints for slack
# simple slack endpoint to read message when bot is mentioned
@slack_event_adapter.on("app_mention")
def user_message(payload):
    event = payload.get("event", {})
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    message = text.split(" ")
    # print(message)
    if message[1] == "ingredient" or message[1] == "ingredients":
        ingredients = message[2:]
        # print(ingredients)
        recipes = make_recipe_by_ingredients(ingredients)
        # print(recipes)
    if message[1] == "random":
        recipe = make_random_recipe()
        print(recipe)
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
    recipes = json.dumps(response.json(), indent=2)
    return recipes


# call to get a random recipe function
def make_random_recipe():
    response = sv.random_recipes()
    recipe = json.dumps(response.json(), indent=2)
    return recipe


if __name__ == "__main__":
    app.run(debug=True)