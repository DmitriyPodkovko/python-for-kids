def msLn(ms, x, years):
    years = years + 1
    for year in range(1, years):
        ms = ms + x
        massaLuna = ms * 0.165
        print('Рік %s вага %s' % (year, massaLuna))

msLn(35, 0.3, 5)
