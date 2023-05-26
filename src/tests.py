import items
import unittest
import genetic_algorithm


class ArtifactTest(unittest.TestCase):

    def test_for_values_below_0(self):
        prop = [-4.0, -8.0]
        self.assertEqual(-4, items.get_value(prop, 0, 0))
        self.assertEqual(-4, items.get_value(prop, 0, 5))
        self.assertEqual(-6, items.get_value(prop, 50, 0))
        self.assertEqual(-7.2, items.get_value(prop, 100, 0))
        self.assertEqual(-7.6, items.get_value(prop, 105, 0))
        self.assertEqual(-7.2, items.get_value(prop, 120, 0))
        self.assertEqual(-7.6, items.get_value(prop, 135, 0))
        self.assertEqual(-8, items.get_value(prop, 150, 0))
        self.assertEqual(-11.6, items.get_value(prop, 155, 0))
        self.assertEqual(-12, items.get_value(prop, 160, 0))
        self.assertEqual(-7.2, items.get_value(prop, 170, 0))
        self.assertEqual(-7.6, items.get_value(prop, 175, 0))

    def test_for_negative(self):
        prop = [0.25, 0.5]
        self.assertEqual(0.25, items.get_value(prop, 0, 0, True))
        self.assertEqual(0.25, items.get_value(prop, 0, 5, True))
        self.assertEqual(0.38, items.get_value(prop, 50, 0, True))
        self.assertEqual(0.45, items.get_value(prop, 100, 0, True))
        self.assertEqual(0.46, items.get_value(prop, 101, 0, True))
        self.assertEqual(0.47, items.get_value(prop, 105, 0, True))
        self.assertEqual(0.45, items.get_value(prop, 120, 0, True))
        self.assertEqual(0.47, items.get_value(prop, 135, 0, True))
        self.assertEqual(0.5, items.get_value(prop, 150, 0, True))
        self.assertEqual(0.72, items.get_value(prop, 155, 0, True))
        self.assertEqual(0.75, items.get_value(prop, 160, 0, True))
        self.assertEqual(0.45, items.get_value(prop, 170, 0, True))
        self.assertEqual(0.47, items.get_value(prop, 175, 0, True))

    def test_for_negative_and_values_below_0(self):
        prop = [-0.8, -1.6]
        self.assertEqual(-0.8, items.get_value(prop, 0, 0, True))
        self.assertEqual(-0.88, items.get_value(prop, 0, 5, True))
        self.assertEqual(-1.2, items.get_value(prop, 50, 0, True))
        self.assertEqual(-1.44, items.get_value(prop, 50, 10, True))
        self.assertEqual(-1.6, items.get_value(prop, 100, 0, True))
        self.assertEqual(-1.68, items.get_value(prop, 105, 0, True))
        self.assertEqual(-1.92, items.get_value(prop, 120, 0, True))
        self.assertEqual(-2.16, items.get_value(prop, 135, 0, True))
        self.assertEqual(-2.4, items.get_value(prop, 150, 0, True))
        self.assertEqual(-2.48, items.get_value(prop, 155, 0, True))
        self.assertEqual(-2.56, items.get_value(prop, 160, 0, True))
        self.assertEqual(-2.72, items.get_value(prop, 170, 0, True))
        self.assertEqual(-2.8, items.get_value(prop, 175, 0, True))

    def test_for_normal_properties(self):
        prop = [0.75, 1.5]
        self.assertEqual(0.75, items.get_value(prop, 0, 0))
        self.assertEqual(0.82, items.get_value(prop, 0, 5))
        self.assertEqual(1.13, items.get_value(prop, 50, 0))
        self.assertEqual(1.35, items.get_value(prop, 50, 10))
        self.assertEqual(1.5, items.get_value(prop, 100, 0))
        self.assertEqual(1.58, items.get_value(prop, 105, 0))
        self.assertEqual(1.8, items.get_value(prop, 120, 0))
        self.assertEqual(2.03, items.get_value(prop, 135, 0))
        self.assertEqual(2.25, items.get_value(prop, 150, 0))
        self.assertEqual(2.33, items.get_value(prop, 155, 0))
        self.assertEqual(2.4, items.get_value(prop, 160, 0))
        self.assertEqual(2.55, items.get_value(prop, 170, 0))
        self.assertEqual(2.63, items.get_value(prop, 175, 0))

    def test_for_negative_extra_properties(self):
        prop = [-0.6, -1.2]
        self.assertEqual(-0.66, items.get_value(prop, 0, 5, extra=True))
        self.assertEqual(-0.99, items.get_value(prop, 50, 5, extra=True))
        self.assertEqual(-1.08, items.get_value(prop, 50, 10, extra=True))
        self.assertEqual(-1.32, items.get_value(prop, 100, 5, extra=True))
        self.assertEqual(-1.39, items.get_value(prop, 105, 5, extra=True))
        self.assertEqual(-1.58, items.get_value(prop, 120, 5, extra=True))
        self.assertEqual(-1.78, items.get_value(prop, 135, 5, extra=True))
        self.assertEqual(-1.98, items.get_value(prop, 150, 5, extra=True))
        self.assertEqual(-2.05, items.get_value(prop, 155, 5, extra=True))
        self.assertEqual(-2.11, items.get_value(prop, 160, 5, extra=True))
        self.assertEqual(-2.24, items.get_value(prop, 170, 5, extra=True))
        self.assertEqual(-2.31, items.get_value(prop, 175, 5, extra=True))


class GeneticTest(unittest.TestCase):
    def test_simple(self):
        container = items.Container("Cocoon Container")
        g = genetic_algorithm.GeneticAlgorithm(container=container, quality=100.0, potential=10)
        g.train_ga()
