# Tasty Recipe Search

Tasty Recipe Search is a utility that allows developers to search recipes with tasty ingredients.

This command line tool allows one to search for new recipes with a few tasty ingredients.
It returns both the recipe and the missing ingredients.

## Prerequisites

Python >= 3.6

.env file with the following environment variables

API_KEY=<< Spoonacular API key >>

API_URL=<< Spoonacular API find by ingredients path >> i.e. https://api.spoonacular.com/recipes/findByIngredients

## Installing Tasty Recipe Search

To setup the project, follow these steps after cloning the repo:
```
pip install -r requirements.txt
```

To setup the project with Docker
- Build the Dockerfile in the root of the project

```
docker build -t tasty-recipe .
```
- Run the docker command
Linux and macOS:
```
docker run --rm -it -v $(pwd):/usr/src/app tasty-recipe python main.py tomato onion

```

Windows:
```
docker run --rm -it -v %cd%\usr/src/app tasty-recipe python main.py tomato onion
```

## Using Tasty Recipe Search

To use Tasty Recipe Search, follow these steps:

```
python main.py ...ingredients

i.e. python main.py onion tomato
```

