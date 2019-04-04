price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for x in price:
    if x == 'apple' or x == 'pear':
        print(x)
        print('price:',price[x])
        print('stock:',stock[x])

total = 0
for i in price:
    total_revenue = price[i] * stock[i]
    total += total_revenue

print("Total revenue = ",total)