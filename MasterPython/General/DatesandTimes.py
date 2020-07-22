# The best way to handle dates and times is to always use UTC and then convert to localised times at the end.
# pytz is python timezone (best module for times)
# A naive time is one which is unaware of its timezone as opposed to an aware time.

import time
import random
import datetime
import pytz

# print(time.time()) #number of seconds since start of epoch
# print(time.gmtime(0))
# print(time.localtime())
# print(time.localtime(time.time()))
# print('-' * 40)
#
# time_here = time.localtime()
# print(time_here)
# print('Year: ', time_here[0], time_here.tm_year)
# print('Month: ', time_here[1], time_here.tm_mon)
# print('Day: ', time_here[2], time_here.tm_mday)
#
# from time import time as my_timer
# from time import perf_counter as my_timer # / this is elapsed time
# from time import process_time as my_timer #/ this is the processor time
#
#
# input('input time to start')
# print()
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
#
# input('press enter to stop')
# end_time = my_timer()
#
# print('Started at: ' + time.strftime('%X', time.localtime(start_time)))
# print('Ended at: ' + time.strftime('%X', time.localtime(end_time)))
# print('your reaction time was {}'.format(end_time - start_time))
#
# print('time()\t\t\t', time.get_clock_info('time'))
# print('perf_counter()\t', time.get_clock_info('perf_counter'))
# print('monotomic()\t\t', time.get_clock_info('monotonic'))
# print('process_time()\t', time.get_clock_info('process_time'))
#
#
# print('the epoch on this system starts at: ', time.strftime('%c', time.gmtime(0)))
# print('the timezone is {0} with an offset of {1}: '.format(time.tzname[0], time.timezone))
#
# if time.daylight !=0 :
#     print('daylight saving is in effect')
#     print('the dst timezone is ' + time.tzname[1])
#
# print('local time is '+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print('utc time is '+ time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
#
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())


#  ============================================================================================================================================
# country = 'Pacific/Guadalcanal'
# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print('the time in {} is {}'.format(country, local_time))
# print('the time utc is {}'.format(datetime.datetime.utcnow()))
#
# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print( x + ': ' + pytz.country_names[x])
#
# for x in sorted(pytz.country_names):
#     print('{}: {}: {}'.format(x, pytz.country_names[x], pytz.country_timezones[x]))
#
# for x in sorted(pytz.country_names): #this return none if empty
#     print('{}: {}: {}'.format(x, pytz.country_names[x], pytz.country_timezones.get(x)))
#
# for x in sorted(pytz.country_names):
#     print('{}: {}:'.format(x, pytz.country_names[x]), end=': ')
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_to_display)
#             print('\t\t\t{}: {}'.format(zone, local_time))
#     else:
#         print('\t\ttimezone not defined')
#  ============================================================================================================================================


# localtime = datetime.datetime.now()
# utctime = datetime.datetime.utcnow()
#
# print('naive localtime is {}'.format(localtime))
# print('naive utc localtime is {}'.format(utctime))
#
# aware_localtime = pytz.utc.localize(localtime).astimezone()
# aware_utctime = pytz.utc.localize(utctime)
#
# print('aware local time {}, timezone {}'.format(aware_localtime, aware_localtime.tzinfo))
# print('aware utc time {}, timezone {}'.format(aware_utctime, aware_utctime.tzinfo))
#
# gap_time = datetime.datetime(2012, 3, 21, 1, 0, 0, 0)
# gap_time_1 = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
# # print(gap_time)
# # print(gap_time.timestamp())
# print(gap_time_1)
# print(gap_time_1.timestamp())
#
# s = 1445733000
# t = s + (60 * 60) #plus 1 hour
#
# gb = pytz.timezone('GB')
# dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb) #before clocks change
# dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb) #after clocks change
#
# print('{} seconds since the epoch is {}'.format(s, dt1))
# print('{} seconds since the epoch is {}'.format(t, dt2))

#  ============================================================================================================================================