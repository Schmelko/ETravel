import unittest
from travel_log import TravelLog
from travel_log_entry import TravelLogEntry


class TestSolution(unittest.TestCase):

    def setUp(self):
        with open('utasadat.txt') as f:
            lines = f.readlines()
        
        self.mcard_log = TravelLog(lines)

    def test_task1(self):
        self.assertEqual(len(self.mcard_log.entries), 699)

    def test_task2(self):
        expected = 699
        result = len(self.mcard_log.ticket_id_unique())
        self.assertEqual(expected, result)        

if __name__ == '__main__':
    unittest.main()