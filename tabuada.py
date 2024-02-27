print('ola, isso é um programa de tabuada ')
tabuada=int(input("Tabuada do numero: "))# a pesssoa digita qual numero que quer ver a tabuada

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
print( '\033[32m_' * 51)
