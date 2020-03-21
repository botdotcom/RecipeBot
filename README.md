# RecipeBot for Slack

This is an extension of my another project 'KitchenCompanion', where I get recipes from Spoonacular API based on a few ingredients as my search terms.

I am building a Slack bot `@recipebot` that responds with a recipe when called in a workspace.

### Usage

NOTE: Add your own API authentication keys in `secret.json` file before running this app.

For now, to invoke this bot, mention it in a channel in the message box as:

```
@recipebot ingredient mango
```

OR 

```
@recipebot ingredients mango
```

For a list of ingredients, you can message as:

```
@recipebot ingredient tomato olives
```

OR

```
@recipebot ingredients tomato olives
```