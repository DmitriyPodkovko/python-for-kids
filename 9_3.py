f = open('C:\\Users\\Acer\\Desktop\\P\\test.txt')
s = f.read()
f.close()
f = open('C:\\Users\\Acer\\Desktop\\P\\testOut.txt', 'w')
f.write(s)
f.close()

import shutil
shutil.copy('C:\\Users\\Acer\\Desktop\\P\\test.txt', 'C:\\Users\\Acer\\Desktop\\P\\testOut2.txt')
