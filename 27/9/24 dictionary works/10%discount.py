prices = {'apple': 100,'banana': 50,'cherry':75,'date': 120}

discount_prices={item:price*0.9 for item,price in prices.items()}

print(discount_prices)