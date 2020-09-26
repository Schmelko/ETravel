from datetime import datetime

class TravelLogEntry:
    '''One log entry.'''

    def __init__(self, line):
        raw = line.split()
        self.stop_id = int(raw[0])
        self.get_on_datetime = datetime.strptime(raw[1], '%Y%m%d-%H%M')
        self.ticket_id = int(raw[2])
        self.ticket_type =  (raw[3])
        if self.isPass():
            self.no_of_ticket_left = int(raw[4])
        else:
            self.ticket_expiration = datetime.strptime(raw[4], '%Y%m%d')

    def isPass(self):
        return self.ticket_type == 'JGY'
