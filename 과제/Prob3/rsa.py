from Crypto.Util.number import *

p, q = getPrime(64), getPrime(64)
N = p * q
e = 0x10001
print(N)

plain = open('flag.txt', 'rb').read()

m = bytes_to_long(plain)
print(p.bit_length())
c = pow(m, e, N)
f = open('output.txt', 'w')

f.write('c = ' + str(c) + '\n')
f.write('N = ' + str(N) + '\n')
f.write('e = ' + str(c) + '\n')

f.close()