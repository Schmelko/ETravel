from datetime import datetime

class TravelLogEntry:
    '''One log entry.'''

    def __init__(self, line):
        self.free_types = set(('NYP', 'RVS', 'GYK'))
        self.discounted_types = set(('TAB', 'NYB'))

        raw = line.split()
        self.stop_id = int(raw[0])
        self.get_on_datetime = datetime.strptime(raw[1], '%Y%m%d-%H%M')
        self.ticket_id = int(raw[2])
        self.ticket_type =  (raw[3])
        if self.is_pass():
            self.ticket_expiration = datetime.strptime(raw[4], '%Y%m%d')
        else:
            self.no_of_ticket_left = int(raw[4])

    def is_pass(self):
        return self.ticket_type != 'JGY'

    def is_rejected(self):
        if self.is_pass():
            return self.get_on_datetime.date() > self.ticket_expiration.date()
        else:
            return self.no_of_ticket_left == 0
    
    def is_free(self):
        return self.ticket_type in self.free_types

    def is_discounted(self):
        return self.ticket_type in self.discounted_types and not self.is_rejected()
