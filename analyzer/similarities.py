import requests
import logging
from analyzer import RECIPE_CONFIG


def calc_simple_similarity(recipe_id, num):
    """Calculate similarities of other recipes based on given id"""
    component_per_recipe = _get_recipe_components()
    recipe_similarities = _calc_jaccard_similarities(
        component_per_recipe[recipe_id], component_per_recipe)
    recipe_similarities = _sort_and_crop(recipe_similarities, num)

    return _make_result(recipe_similarities)


def _make_result(similarities):
    result = set()
    for s in similarities:
        result.append(s['id'])
    return result


def _jaccard_similarity_set(set1, set2):
    intersection = len(list(set1.intersection(set2)))
    union = (len(set1) + len(set2)) - intersection
    if union > 0:
        return float(intersection) / union
    else:
        return 1.0


def _take_score(element):
    return element['score']


def _sort_and_crop(scores, num):
    scores.sort(key=_take_score, reverse=True)
    return scores[:num]


def _calc_jaccard_similarities(reference_recipe, component_per_recipe):
    recipe_similarities = []
    for val in component_per_recipe.values():
        recipe_similarities = _append_recipe_similarity(
            reference_recipe, recipe_similarities, val)
    return recipe_similarities


def _append_recipe_similarity(reference_recipe, recipe_similarities, val):
    if reference_recipe['id'] != val['id']:
        score = _jaccard_similarity_set(
            reference_recipe['components'], val['components'])
        recipe_similarities.append({'id': val['id'], 'score': score})
    return recipe_similarities


def _get_recipe_components():
    component_per_recipe = dict()  # np.array([])

    r = requests.get(RECIPE_CONFIG.RECIPE_SERVER + '/api/v1/recipes')
    for idx, recipe_id in enumerate(r.json()):
        r = requests.get(RECIPE_CONFIG.RECIPE_SERVER +
                         '/api/v1/recipes/r/' + recipe_id)
        components = set()
        try:
            for component in r.json()['components']:
                components.add(component['name'])
        except:
            logging.error("Could not add valid recipe" + str(recipe_id))
        component_per_recipe[recipe_id] = {
            'id': recipe_id, 'components': components}

    return component_per_recipe
