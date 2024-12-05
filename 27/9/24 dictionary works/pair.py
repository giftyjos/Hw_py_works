fruit=['apple','banana','cherry']

prices=[100,50,150]

fruit_prices={fruit:price for fruit,price in zip(fruit,prices)}
print(fruit_prices)