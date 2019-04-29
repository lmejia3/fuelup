from datetime import date
from Modules.DatabaseConnector import DatabaseConnector as db
"""
module responsible for deciding the pricing for different usres. It puts into account the history of
transactions, trends, profit margin, and location.
"""

def getQuote(form):
    rate = 1.5
    hist = getUserHistoryFactor(form['id'])
    event = getEventFactor()
    loc = getLocationFactor(form['state'])
    amm = getAmountFactor(form['gallons'])
    prof = getProfitMargin()

    price = (form['gallons'] * rate)*(loc - hist + amm + prof + event + 1)
    print('quote: ' + str(price))

    form['price'] = price
    form['history'] = hist
    form['season'] = event
    form['location'] = loc
    form['amount'] = amm
    form['profit'] = prof
    form['rate'] = rate

    return price

def getUserHistoryFactor(user):
    q = 'SELECT * FROM Invoice WHERE Username_ID = %s AND Paid = 1' \
        % (user)
    curProfile = db.runQuery(q)
    if (len(curProfile) > 0):
        return 0.01
    return 0.0

def getEventFactor():
    d = date.today()
    y = d.year
    s_summer = date(y, 6, 21)
    e_summer = date(y, 9, 22)
    if(d >= s_summer and d <= e_summer):
        return 0.04
    else:
        return 0.03

def getAmountFactor(amount):
    if (amount >= 1000):
        return 0.02
    else:
        return 0.03

def getLocationFactor(state):
    if(state == 'TX'):
        return 0.02
    else:
        return 0.04

def getProfitMargin():

    return 0.1