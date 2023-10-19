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


    def test_message_length_1(self):
        message = "#korea #usa #news Deadly storms and floods in Sardinia: At least nine people are killed and a number are missi...  http://t.co/PQsiQsTEZX"
        expected = 17
        actual = du._get_message_length(message)
        self.assertEqual(expected, actual)


    def test_message_length_2(self):
        message = "RT @BBCBreaking: Photo shows #helicopter crash at #Clutha pub in Glasgow http://t.co/cYMa37HdjM &amp; http://t.co/gY03CIFj80"
        expected = 9
        actual = du._get_message_length(message)
        self.assertEqual(expected, actual)