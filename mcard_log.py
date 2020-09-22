from mcard_log_entry import McardLogEntry

class McardLog:

    def __init__(self, lines):
        self.entries = [McardLogEntry(line) for line in lines]

    def __str__(self):
        return "{} entries in mcard_log".format(len(self.entries))
