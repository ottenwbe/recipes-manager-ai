import os
import unittest

from analyzer import config
from analyzer.config import DEFAULT_RECIPE_SERVER, RecipeStatsConfig


class TestConfig(unittest.TestCase):
    def test_default_config(self):
        cfg1 = RecipeStatsConfig()
        cfg1.make_config()
        self.assertEqual(cfg1.RECIPE_SERVER, DEFAULT_RECIPE_SERVER)

    def test_singleton_config(self):
        cfg1 = RecipeStatsConfig()
        cfg1.RECIPE_SERVER = "test"
        cfg2 = RecipeStatsConfig()
        self.assertEqual(cfg2.RECIPE_SERVER, "test")

    def test_read_yml_config(self):
        try:
            with open('config.yml', 'w') as writer:
                writer.write(config.RECIPE_SERVER + ": ahost:123")
            cfg1 = RecipeStatsConfig()
            cfg1.make_config()
            self.assertEqual(cfg1.RECIPE_SERVER, "ahost:123")
        finally:
            os.remove('config.yml')


if __name__ == '__main__':
    unittest.main()
