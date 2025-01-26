def stockPricePredic():
    arr = list(map(int, input("Enter the stock prices separated by space: ").split()))
    min_price = float('inf')
    max_profit = 0

    for price in arr:
        min_price = min(min_price, price)  # Update min_price if we find a lower price
        max_profit = max(max_profit, price - min_price)  # Calculate the maximum profit so far

    print("Maximum profit:", max_profit)
stockPricePredic()