from flask import request
from analyzer import app, similarities


@app.route("/")
def root():
    """Root Route"""
    return 'Recipes Analyzer'


@app.route("/api/v1/recommendation/<recipe_id>/components")
def recommend_recipe(recipe_id):
    """Recommend n recipes based on an id."""
    num = request.args.get('num')
    num = ensure_num(num)
    r = similarities.calc_simple_similarity(recipe_id, num)
    return r


def ensure_num(num):
    if (num is None) or (int(num) < 1):
        num = 1
    return int(num)
