from mcard_log import McardLog

with open('utasadat.txt') as f:
    lines = f.readlines()
    mcard_log = McardLog(lines)

print(mcard_log)

print(len(mcard_log.ticket_id_unique()))
