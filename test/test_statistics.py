import unittest
from app.statistics import DataCapture
from app.statistics import StatsEngine


class TestDataCapture(unittest.TestCase):
    def test_add(self):
        # data_capture = 1, 2, 2, 3, 3, 3, 4, 4 ...
        data_capture = DataCapture()
        inputs = range(2, 1000)
        numbers_dict = {}
        for i in inputs:
            numbers_dict[i] = i
            for _ in range(i):
                data_capture.add(i)
        data_capture.add(1)
        numbers_dict[1] = 1
        self.assertDictEqual(numbers_dict, data_capture.numbers_dict)

    def test_build_stats(self):
        data_capture = DataCapture()
        self.stats_engine = data_capture.build_stats()
        self.assertIsInstance(self.stats_engine, StatsEngine)


class TestStatsEngine(unittest.TestCase):
    # n*(n+1)/2 or other cumulative formula can be applied
    @ classmethod
    def setUpClass(cls):
        data_capture = DataCapture()
        inputs = range(1, 1000)

        for i in inputs:
            for _ in range(i):
                data_capture.add(i)
        cls.stats_engine = data_capture.build_stats()

    def test_less(self):

        self.assertEqual(self.stats_engine.less(1), 0)  # Lower edge case
        self.assertEqual(self.stats_engine.less(2), 1)  # Lower+1 edge case
        self.assertEqual(self.stats_engine.less(999),
                         998 * 999/2)  # Upper edge case (n*(n+1)/2)
        self.assertEqual(self.stats_engine.less(20), 19*20/2)  # Normal case

    def test_greater(self):
        self.assertEqual(self.stats_engine.greater(1),
                         999*1000/2 - 1)  # Lower edge case
        self.assertEqual(self.stats_engine.greater(999), 0)
        # Upper edge case
        self.assertEqual(self.stats_engine.greater(998), 999)
        # Upper-1 edge case
        self.assertEqual(self.stats_engine.greater(
            20), 999*1000/2 - 20*21/2)  # Normal case

    def test_between(self):
        self.assertEqual(self.stats_engine.between(1, 1), 1)
        self.assertEqual(self.stats_engine.between(999, 999), 999)
        self.assertEqual(self.stats_engine.between(
            1, 999), 999*1000/2)  # Edge case
        self.assertEqual(self.stats_engine.between(999, 1),
                         999*1000/2)  # Inverted edge case
        self.assertEqual(self.stats_engine.between(
            60, 62), 60 + 61 + 62)  # Normal case
