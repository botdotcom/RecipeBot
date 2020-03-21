import requests
import json
"""this file contains the actual calls to Spoonacular API"""

# get recipe title and detailed ingredients from mentioned ingredients
def recipes_by_ingredients(ingredients):
    with open("secret.json", "r") as f:
        key = json.load(f)

    # prepare the parameters to put in the url
    make_param = ""
    for i in range(len(ingredients)):
        make_param += ingredients[i]
        if i == len(ingredients) - 1:
            break
        make_param += ",+"

    url = "https://api.spoonacular.com/recipes/findByIngredients?" \
          "ingredients={}" \
          "&number=3&limitLicense=true&ranking=1&ignorePantry=true" \
          "&apiKey={}".format(make_param, key['spoon_key'])

    response = requests.get(url)
    return response


# get a reipe at random
def random_recipes():
    with open("secret.json", "r") as f:
        key = json.load(f)

    url = "https://api.spoonacular.com/recipes" \
          "/random?number=1" \
          "&apiKey={}".format(key['spoon_key'])

    response = requests.get(url)
    return response


# get detailed recipe from recipe id extracted somewhere
def recipe_information_by_id(recipe_id):
    with open("secret.json", "r") as f:
        key = json.load(f)

    url = "https://api.spoonacular.com/recipes" \
          "/{}/information?includeNutrition=true" \
          "&apiKey={}".format(recipe_id, key['spoon_key'])

    response = requests.get(url)
    return response