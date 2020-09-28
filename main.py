from travel_log import TravelLog

with open('utasadat.txt') as f:
    lines = f.readlines()
    travel_log = TravelLog(lines)

print(travel_log)

print(len(travel_log.ticket_id_unique()))

notifiables = travel_log.find_notifiables_of_coming_expiration(3)
notifiables_content = tuple("{}\t{}".format(notifiable.ticket_id, notifiable.ticket_expiration.strftime('%Y-%m-%d')) for notifiable in notifiables)

with open("figyelmeztetes.txt", "w") as f:
    f.writelines('\n'.join(notifiables_content))
