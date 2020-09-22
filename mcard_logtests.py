import unittest
from mcard_log import McardLog
from mcard_log_entry import McardLogEntry


class TestSolution(unittest.TestCase):

    def setUp(self):
        with open('utasadat.txt') as f:
            lines = f.readlines()
        
        self.mcard_log = McardLog(lines)

    def test_task1(self):
        self.assertEqual(len(self.mcard_log.entries), 699)

if __name__ == '__main__':
    unittest.main()