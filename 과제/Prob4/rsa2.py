from Crypto.Util.number import *

p, q = getPrime(512), getPrime(512)
e = 0x10001
N = p * q
phi = (p-1) * (q-1)
d = inverse(e,phi)

f = open('output.txt','w')
f.write('*** mission : recover p , q ***\n\n')
f.write('N = '+str(N)+ '\n')
f.write('e = '+str(e)+ '\n')
f.write('d = '+str(d)+ '\n')
