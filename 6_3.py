list1 = ['exm1', 'exm2', 'exm3', 'exm4', 'exm5']
for i in range(1, 6):
    print('%s' % i, list1[i-1])

x = 1
for i in list1:
    print('%s %s' % (x, i))
    x = x + 1
