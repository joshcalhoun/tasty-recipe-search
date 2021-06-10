from dotenv import load_dotenv
import argparse
import requests
import os

load_dotenv()


def get_recipes(ingredients):
    # Get the api key from environment variables
    api_key = os.environ.get('API_KEY', '')
    api_host = os.environ.get('API_URL', '')

    r = requests.get(f'{api_host}?apiKey={api_key}&ingredients={",".join(ingredients)}')
    return r.json()


def get_most_liked_recipe(recipes):
    recipe = {}

    # Find the most popular recipe by getting the result with the largest likes
    if len(recipes):
        recipe = max(recipes, key=lambda x: x.get('likes', 0))

    return recipe


def main(opts):
    if len(opts.ingredients) == 0:
        parser.error('Ingredients argument(s) are required.')

    # Call spoonacular api with
    recipes = get_recipes(opts.ingredients)

    # Return recipes with highest likes
    most_liked_recipe = get_most_liked_recipe(recipes)

    # Output recipe and missing ingredients
    print(f'Recipe:\n{most_liked_recipe.get("title")}\n')

    missed_ingredients = most_liked_recipe.get('missedIngredients', [])
    if missed_ingredients:
        print('Missing Ingredients:')

        for missed_ingredient in missed_ingredients:
            print(f'{missed_ingredient.get("originalString", "")}')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # Required ingredient(s) argument
    parser.add_argument("ingredients", help="Required argument ingredients as a space separated list.", nargs="*")

    args = parser.parse_args()
    main(args)

