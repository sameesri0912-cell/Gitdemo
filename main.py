import datetime as dt
import random

now=dt.datetime.now()
year=now.year
month=now.month
day=now.day
print(day)
week_day=now.strftime("%A")
print(week_day)

with open("quotes.txt", 'w' )as f:
    f.write("Honesty is the best policy\nBe good Do good\nTime is Money\nA friend in need is a friend in deed")


with open("quotes.txt", 'r') as fw:
    quotes_list=list(fw.readlines())
print(quotes_list)

if week_day=="Thursday":
    quote_for_day=random.choice(quotes_list)
    print(quote_for_day)
