import pickle
favoritethings = ['football', 'cars', 'rest']
f = open('favorites.dat', 'wb')
pickle.dump(favoritethings, f)
f.close

f = open('favorites.dat', 'rb')
favoritethings = pickle.load(f)
print(favoritethings)
