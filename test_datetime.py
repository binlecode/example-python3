
from datetime import datetime, timezone



# Unlike the time module, the datetime module has facilities for reliably converting
# from one local time to another local time.

# a naive datetime (without timezone info)
now = datetime.now()
print('localtime: ', now)  
# convert naive datetime to zoned time using system default timezone
print('localtime with system timezone: ', now.astimezone())  


# The preferred way of dealing with times is to always work in UTC, converting to localtime only when 
# generating output to be read by humans.

# in terminal run `pip install pytz`
import pytz

from pytz import timezone

tz_utc = pytz.utc
assert tz_utc.zone == 'UTC'

tz_est = timezone('US/Eastern')
tz_pt = timezone('US/Pacific')

now_utc = tz_utc.normalize(now.astimezone())

# astimezone method is useful to switch timezones
now_est = now_utc.astimezone(tz_est)
now_pt = now_utc.astimezone(tz_pt)

print('now_utc: ', now_utc)
print('now_est: ', now_est)
print('now_pt:  ', now_pt)

assert now_pt.astimezone(tz_utc) == now_est.astimezone(tz_utc)
