# MIT License
#
# Copyright (c) 2021 Beate Ottenwälder
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests
import logging
from analyzer import RECIPE_CONFIG

class Client:

    def __init__(self):
        pass

    def get_recipe_components():
        component_per_recipe = dict()  

        r = requests.get(RECIPE_CONFIG.RECIPE_SERVER + '/api/v1/recipes')

        logging.info("get recipes from " +
                     RECIPE_CONFIG.RECIPE_SERVER + '/api/v1/recipes')

        if not r.ok:
            logging.error("Could not get recipes: " + r.status_code)
            return component_per_recipe

        for idx, recipe_id in enumerate(r.json()['recipes']):
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

        logging.info(component_per_recipe)

        return component_per_recipe
