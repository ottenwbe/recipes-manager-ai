# recipes-recommender

[![Python application](https://github.com/ottenwbe/recipes-manager-recommender/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/ottenwbe/recipes-manager-recommender/actions/workflows/python-package.yml)

Micro-Service that analyzes all recipes of recipe-manager.

## Dependencies

````bash
pip install -r requirements.txt
````

## Run with Flask

````bash
FLASK_ENV=development FLASK_APP="recipes-analyzer" flask run
````