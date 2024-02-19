from datetime import *

now = datetime.now()

date2 = now - timedelta(days=5)
print("five days ago:", date2)


yesterday = now - timedelta(days=1)

tomorrow = now + timedelta(days=1)

print("yesterday:", yesterday)
print("today:", now)
print("tomorrow:", tomorrow)

without_microseconds = now.replace(microsecond=0)
print("without microseconds:", without_microseconds)


date2 = now - timedelta(days=100)

diff = (now - date2).total_seconds()
print("difference in seconds:", diff)

