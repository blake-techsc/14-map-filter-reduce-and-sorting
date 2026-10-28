prices = [25.00, 50.00, 75.00, 100.00, 150.00]

def discount(price):
    discount = price * -0.2
    return price + discount

printDiscount = list(map(discount, prices))

print("Original prices:")
print(prices)
print("Discounted prices:")
print(printDiscount)