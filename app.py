from flask import Flask, render_template, request
# from slack import WebClient
import json
import service as sv

# this is the main flask app with my endpoints
app = Flask(__name__)


# default page where app lands
@app.route('/recipes')
def default():
    return render_template("home.html")


# get recipes from list of ingredients
@app.route('/recipes/ingredients', methods=['GET'])
def get_recipes_by_ingredients():
    ingredients = request.args.getlist('items')
    response = sv.recipes_by_ingredients(ingredients)
    recipes = json.dumps(response.json(), indent=2)
    print(recipes)
    return render_template("searchresults.html")


# get recipes related to the current recipe (by id)
@app.route('/recipes/<recipeid>/related')
def get_related_recipes(recipeid):
    response = sv.related_recipes(recipeid)
    recipes = json.dumps(response.json())
    # print(recipes)
    return render_template("searchresults.html")


# get a random recipe
@app.route('/recipes/random')
def get_random_recipes():
    response = sv.random_recipes()
    recipes = json.dumps(response.json())
    print(recipes)
    return render_template("searchresults.html")


if __name__ == "__main__":
    app.run(debug=True)