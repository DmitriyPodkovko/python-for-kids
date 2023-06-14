massa = 30
massaLuna = None
for i in range(0, 15):
    massaLuna = (massa + i) * 0.165
    print(i+1, massaLuna)

massa = 30
for year in range(1, 16):
    massa = massa + 1
    massaLuna = massa * 0.165
    print('Рік %s вага %s' % (year, massaLuna))

