import sys
def msLn():
    print("Введіть свою вагу на Землі")
    massa = float(sys.stdin.readline())
    print("Введіть кількість, на яку збільшуватиметься вага на Землі")
    x = float(sys.stdin.readline())
    print("Введіть кількість років")
    years = int(sys.stdin.readline())
    years = years + 1
    for year in range(1, years):
        massa = massa + x
        massaLuna = massa * 0.165
        print('Рік %s вага %s' % (year, massaLuna))

msLn()

