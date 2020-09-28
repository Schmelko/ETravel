from travel_log_entry import TravelLogEntry

class TravelLog:

    def __init__(self, lines):
        self.entries = [TravelLogEntry(line) for line in lines]

    def __str__(self):
        return "{} entries in travel_log".format(len(self.entries))

    def ticket_id_unique(self):
        return set(entry.ticket_id for entry in self.entries)

    def rejected_travels(self):        
        return tuple(entry for entry in self.entries if entry.is_rejected())

    def find_stop_with_most_entries(self):
        stop_ids = set(entry.stop_id for entry in self.entries)
        entries_by_stops = {stop_id:self.get_entries_by_stop_id(stop_id) for stop_id in stop_ids}
        max_entries = max(tuple(entries for entries in entries_by_stops.values()))
        for stop_id in stop_ids:
            if entries_by_stops[stop_id] == max_entries:
                return (stop_id, max_entries)
        
    def get_entries_by_stop_id(self, stop_id):
        return len(tuple(entry for entry in self.entries if entry.stop_id == stop_id))
    
    def find_free_travels(self):
        return tuple(entry for entry in self.entries if entry.is_free())

    def find_discounted_travels(self):
        return tuple(entry for entry in self.entries if entry.is_discounted())

    def find_differences(self):
        return tuple(entry for entry in self.entries if entry.is_difference_between_expirationandgeton())
