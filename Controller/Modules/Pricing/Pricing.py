from datetime import date
"""
module responsible for deciding the pricing for different usres. It puts into account the history of
transactions, trends, profit margin, and location.
"""

def getQuote(form):
    rate = 1.5
    hist = getUserHistoryFactor(1)
    event = getEventFactor()
    loc = getLocationFactor(form['state'])
    amm = getAmountFactor(form['gallons'])

    return 0.0

def getUserHistoryFactor(user):

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

    return 0.0