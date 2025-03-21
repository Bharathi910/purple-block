def max_profit(prices):
    if not prices:
        return None
    
    min_price = prices[0]
    max_profit = 0
    best_buy = 0
    best_sell = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            best_buy = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            best_sell = i

    return (prices[best_buy], prices[best_sell])


#Example

prices = [5,2,1,6,9,7]
result = max_profit(prices)
print("best buy price", result[0],"best sell price:", result[1])