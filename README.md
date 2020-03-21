# RecipeBot for Slack

This is an extension of my another project 'KitchenCompanion', where I get recipes from Spoonacular API based on a few ingredients as my search terms.

I am building a Slack bot `@recipebot` that responds with a recipe when called in a workspace. You can check out the demo [here](https://youtu.be/VFk69zRmLHk)

### Usage:

NOTE: Add your own API authentication keys in `secret.json` file before running this app.

For now, to invoke this bot, mention it in a channel in the message box as:

```
@recipebot ingredient mango
```

OR 

```
@recipebot ingredients mango
```

For more than one ingredient, you can message as:

```
@recipebot ingredient tomato olives
```

OR

```
@recipebot ingredients tomato olives
```

To just get any random recipe, message as:

```
@recipebot random
```

#### Future work:
1. Recipebot only responds to above messages. I want to make it more life-like so that it can respond to something like `hey @recipebot, can you get me a cool salad recipe?` I hope to do it with something like DialogFlow.
2. Needless to say, this slack bot only makes use of `app_mention` slack event and `chat.postMessage` slack method for now. I want to add more ways communication to this bot in slack.