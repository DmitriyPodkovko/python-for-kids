def msLn(ms, x):
    for year in range(1, 16):
        ms = ms + x
        massaLuna = ms * 0.165
        print('Рік %s вага %s' % (year, massaLuna))

msLn(40, 0.5)
