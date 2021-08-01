import talib
import yfinance as yf

from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
oneYearFromToday = today + relativedelta(years=-1)

today = date.today()
print("Today's date:", today, oneYearFromToday)

data = yf.download("SPY", start=oneYearFromToday, end=today)

morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

data['Morning Star'] = morning_star
data['Engulfing'] = engulfing

engulfing_days = data[data['Engulfing'] != 0]

print(engulfing_days)
