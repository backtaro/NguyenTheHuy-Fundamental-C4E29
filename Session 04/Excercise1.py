inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = 'seashell', 'strange berry', 'lint'

for i in inventory:
    if i == 'backpack':
        inventory['backpack'].remove('dagger')

inventory['gold'] += 50
 
print(inventory)