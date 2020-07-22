import datetime
import pytz

available_zones = { '1' : 'Indian/Mayotte',
                    '2' : 'Africa/Johannesburg',
                    '3' : 'Asia/Damascus',
                    '4' : 'Europe/Amsterdam',
                    '5' : 'Africa/Maputo',
                    '6' : 'America/Mazatlan',
                    '7' : 'Pacific/Saipan',
                    '8' : 'Africa/Bamako',
                    '9' : 'Europe/Luxembourg'
                    }

print('please select a timezone (or enter 0 to quit')
for place in sorted (available_zones):
    print('\t\t {} {}'.format(place, available_zones[place]))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys(): #1-9
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print('the time in {} is {} {}'.format(available_zones[choice],world_time.strftime('%A %x %X %z'),world_time.tzname()))
        print('local time is {}'.format(datetime.datetime.now().strftime('%A %x %X')))
        print('utc time is {}'.format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()