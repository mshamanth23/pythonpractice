import datetime as dt
from datetime import timedelta
x=dt.datetime.now()
print("Current time is",x)
y=dt.datetime.now()+timedelta(days=3)
print(y)
z=dt.datetime.now()-timedelta(days=1)
print("Yesterday's date is",z)
c=dt.datetime.now()+timedelta(days=1)
print("Tommorrows date is",c)
