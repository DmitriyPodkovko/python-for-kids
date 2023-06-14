c = '''Це якщо не ти дуже це хороший читаєш спосіб то заховати щось повідомлення негаразд'''
print(c)
print(dir(c))
help(c.split)
lst = c.split(' ')
print(lst)
for i in range(1, len(lst), 2):
	print(lst[i])

