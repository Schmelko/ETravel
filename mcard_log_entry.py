class McardLogEntry:
    '''One log entry.'''

    def __init__(self, line):
        raw = line.split()
        self.day = int(raw[0])
        self.date = raw[1]
        self.time = raw[2]
        self.mcardnumber = int(raw[3])
        self.mcardtype = raw[4]
        self.valid = raw[5]
        
  