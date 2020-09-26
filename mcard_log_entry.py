class TravelLogEntry:
    '''One log entry.'''

    def __init__(self, line):
        raw = line.split()
        self.stop_id = int(raw[0])
        self.get_on_datetime = raw[1]
        self.ticket_id = int(raw[2])
        self.ticket_type =  (raw[3])
        self.ticket_expiration = raw[4]
        
  