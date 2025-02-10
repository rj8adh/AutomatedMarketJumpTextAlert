from evaluateStockPerformance import evalStockPerformance
from getStockPortfolio import getStockPortfolio
from sendMessage import sendTextMessage
import time

phoneNum = input("\nEnter the phone number you want alerts to for the duration this script is running: ")
carrier = input("\nEnter the mobile carrier of the phone number you gave: ")

stockPortf = getStockPortfolio(False) # Set arg to True to load from stockData.json

while True:
    # Looping through every stock
    for i in reversed(range(len(stockPortf))):
        stock = stockPortf[i]
        ticker = list(stock)[0]

        targetReached, moneyInStock = evalStockPerformance(stock)
        print(f"You currently have ${moneyInStock} in {ticker.upper()}")

        # Checking and sending message if the stock target was reached
        if (targetReached): 

            targetReachedMessage = f"You hit your stock target for {ticker.upper()}. You currently have: {moneyInStock} in this stock"
            print(targetReachedMessage)
            print(type(targetReachedMessage))

            sendTextMessage(phoneNum, carrier, targetReachedMessage)

            del stockPortf[i] # Deleting the item from the stock portfolio so it doesn't keep spam texting the user about the same stock
            
            time.sleep(300) # Making the script run once every 5 mins to accomodate stmplib restrictions