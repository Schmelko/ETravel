import unittest
from travel_log import TravelLog
from travel_log_entry import TravelLogEntry


class TestSolution(unittest.TestCase):

    def setUp(self):
        with open('utasadat.txt') as f:
            lines = f.readlines()
        
        self.travel_log = TravelLog(lines)

    def test_task1(self):
        self.assertEqual(len(self.travel_log.entries), 699)

    def test_task2(self):
        expected = 699
        result = len(self.travel_log.ticket_id_unique())
        self.assertEqual(expected, result)
    
    def test_task3(self):
        expected = 21
        results = self.travel_log.rejected_travels()
        result = len(results)
        self.assertEqual(expected, result)

    def test_task4(self):
        expected_passengers = 39
        expected_stop_nr = 8
        result = self.travel_log.find_stop_with_most_entries()
        self.assertEqual((expected_stop_nr, expected_passengers), result)

    def test_task5(self):
        expected_free = 133
        expected_discounted = 200
        result_free = len(self.travel_log.find_free_travels())
        result_discounted = len(self.travel_log.find_discounted_travels())
        self.assertEqual(expected_free, result_free)
        self.assertEqual(expected_discounted, result_discounted)
    
    def test_task7(self):
        expected = 38
        result = len(self.travel_log.find_notifiables_of_coming_expiration(3))
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
