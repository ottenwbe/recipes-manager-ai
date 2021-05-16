from flask import Flask
from analyzer.config import RecipeStatsConfig

RECIPE_CONFIG = None


def configure_app():
    recipe_config = RecipeStatsConfig()
    recipe_config.make_config()
    global RECIPE_CONFIG
    RECIPE_CONFIG = RecipeStatsConfig()


app = Flask("recipes-analyzer")
configure_app()

from analyzer import controller
