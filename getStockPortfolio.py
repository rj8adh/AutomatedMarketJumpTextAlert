import json

def getStockPortfolio(loadData: bool = False):
    stockAndData = [] # List of dictionaries (allows for multiple alerts to be set for the same stock)

    print("\nGetting Stock Portfolio...\n")

    if (not loadData):
        stockToWatch = input("Enter the first stock ticker in your portfolio, or QUIT to quit: ").upper()
        if (stockToWatch.lower() != "quit"):

            watchLineType = input("Is this watchlist a Top line or Bottom line?(Enter T for Top, and B for Bottom)") # Lets us know if we should alert them if price goes under or over the target
            stockShares = input(f"Enter the amount of shares of {stockToWatch} you have: ")
            stockTargetPrice = input("Enter your target price for the stock alert: ")

            stockAndData.append({stockToWatch : [watchLineType, stockShares, stockTargetPrice]})
        else:
            return "Quit Program"
        
        while True:

            stockToWatch = input("Enter the next stock ticker in your portfolio, or QUIT to quit: ").upper()
            if (stockToWatch.lower() != "quit"):

                watchLineType = input("Is this watchlist a Top line or Bottom line?(Enter T for Top, and B for Bottom) ").lower()
                stockShares = input(f"Enter the amount of shares of {stockToWatch} you have: ")
                stockTargetPrice = input("Enter your target price for the stock alert: ")
                
                stockAndData.append({stockToWatch : [watchLineType, stockShares, stockTargetPrice]})
            else:
                break
        
        jsonFileSave = input("Would you like to save your data to a json file? Respond with Y or N: ").lower()
        if (jsonFileSave == "y"):
            with open("stockData.json", "w") as file:
                json.dump(stockAndData, file)
            file.close()

    else:
        with open("stockData.json") as file:
            stockAndData = json.load(file)

    return stockAndData

print(getStockPortfolio(True))