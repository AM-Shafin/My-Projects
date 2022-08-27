movies = ['Star Wars', 'Gandhi', 'Casablanca', 'Shawshank Redemption', 'Toy Story', 'Gone with the Wind',
          'Citizen Kane', "It's a wonderful life", 'The Wizard of Oz', 'Gattaca', 'Rear Window', 'Ghostbusters',
          'To Kill A Mockingbird', 'Good Will Hunting', '2001: A Space Odyssey', 'Raiders of the Lost Ark',
          'Groundhog Day', 'Close Encounters of the Third Kind']

gmovies = []
for title in movies:
    if title.startswith("G") or title.startswith("g"):
        gmovies.append(title)

print(gmovies)

# List comprehension methode

gmovies = [title for title in movies if title.startswith('G')]
print(gmovies)

# List comprehension that stores name of currencies that values over 99 bucks per $1
exchange = [('EUR', 0.869335), ('JPY', 113.0005), ('GBP', 0.760425), ('AUD', 1.40553), ('CAD', 1.29406),
            ('CHF', 0.99148), ('CNY', 6.9228), ('SEK', 9.09429), ('NZD', 1.54148), ('MXN', 18.99626), ('SGD', 1.3809)]
high_val = [cur for (cur, val) in exchange if val > 99.00]
print(high_val)


#Cartesian porduct: if set A = {1, 2} and set B = {x, y}, then AxB = {(1, x), (1, y), (2, x), (2, y)}
A = [1, 3, 5, 7, 9]
B = ['A', 'E', 'I', 'O', 'U']

cart_pro = [(a, b) for a in A for b in B]
print(cart_pro)