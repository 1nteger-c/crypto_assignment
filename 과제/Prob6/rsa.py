from Crypto.Util.number import *

plain = open('flag.txt', 'rb').read()
m = bytes_to_long(plain)

f = open("output.txt",'w')

for i in range(7):
    p = getPrime(512)
    q = getPrime(512)
    N = p * q
    e = 7
    c = pow(m,e,N)
    f.write('N = ' + str(N) + '\n')
    f.write('c = ' + str(c) + '\n')
    f.write('e = ' + str(e) + '\n')
f.close()