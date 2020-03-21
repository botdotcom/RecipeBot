import requests
import json
# this file contains the actual calls to Spoonacular API

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

# not working
def related_recipes(recipe_id):
    with open("secret.json", "r") as f:
        key = json.load(f)

    url = "https://api.spoonacular.com/recipes/{}" \
          "/similar" \
          "&apiKey={}".format(recipe_id, key['spoon_key'])

    response = requests.get(url)
    return response


def random_recipes():
    with open("secret.json", "r") as f:
        key = json.load(f)

    url = "https://api.spoonacular.com/recipes" \
          "/random?number=1" \
          "&apiKey={}".format(key['spoon_key'])

    response = requests.get(url)
    return response