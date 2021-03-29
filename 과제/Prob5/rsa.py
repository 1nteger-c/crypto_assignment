from Crypto.Util.number import *

p, q = getPrime(512), getPrime(512)
N = p*q
e = 3
plain = open('flag.txt', 'rb').read()
m = bytes_to_long(plain)
c = pow(m,e,N)

f = open('output.txt','w')
f.write('c = '+str(c) + '\n')
f.write('N = '+str(N) + '\n')
f.write('e = '+str(e) + '\n')