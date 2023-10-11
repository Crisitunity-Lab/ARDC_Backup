import unittest

import src.structure_extractor.data_utils as du


class TestStructureExtractor(unittest.TestCase):

    def test_year_calc(self):
        event = "2013_NY_train_crash"
        expected = "2013"
        actual = du._get_year_of_crisis(event)
        self.assertEqual(expected, actual)

    
    def test_country_mapping(self):
        event = "2013_NY_train_crash"
        expected = "US"
        actual = du._get_country_of_crisis(event)
        self.assertEqual(expected, actual)

    
    def test_event_mapping(self):
        event = "2013_NY_train_crash"
        expected = "Train Crash"
        actual = du._get_crisis_type(event)
        self.assertEqual(expected, actual)