import yfinance as yf

def evalStockPerformance(stockData: dict):
    stockTicker = stockData.keys()

    # Convert stockTicker to a string
    stockTicker = list(stockTicker)[0]

    # Making sure the stock ticker is valid
    try:
        ticker = yf.Ticker(stockTicker).info
        currentStockPrice = ticker['currentPrice']
    except:
        print("ERROR: Invalid Stock Ticker For Stock:", stockTicker)
        return
    
    # Assigning all stock info variables
    print(f"\n{currentStockPrice}")
    targetType = stockData[stockTicker][0]
    currentMoney = currentStockPrice * stockData[stockTicker][1]
    targetPrice = stockData[stockTicker][2]

    # Checking what type of target the stock has been given and returning the appropriate values
    if targetType.lower() == "t":
        if currentMoney >= targetPrice:
            return True, currentMoney
        return False, currentMoney
    
    elif stockData[stockTicker][0].lower() == "b":
        if currentMoney <= targetPrice:
            return True, currentMoney
        return False, currentMoney
    
    else:
        print("Invalid target type:", targetType)
        return

# The following code is in case you want to test the function yourself:
# print(evalStockPerformance({"grergegr": ["T", "24.3", "4000"]}))