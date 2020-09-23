from mcard_log_entry import McardLogEntry

class McardLog:

    def __init__(self, lines):
        self.entries = [McardLogEntry(line) for line in lines]

    def __str__(self):
        return "{} entries in mcard_log".format(len(self.entries))

    def ticket_id_unique(self):
        return set(entry.ticket_id for entry in self.entries)

     
