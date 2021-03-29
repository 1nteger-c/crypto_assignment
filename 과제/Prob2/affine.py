
def affine(plain, key1, key2):
    cipher = ''
    for i in range(len(plain)):
        tmp = plain[i]
        if(tmp.isupper()):
            tmp = ord(tmp) - ord('A')
            tmp = tmp * key1 + key2
            tmp = tmp % 26 + ord('A')
            cipher += chr(tmp)
        elif(tmp.islower()):
            tmp = ord(tmp) - ord('a')
            tmp = tmp * key1 + key2
            tmp = tmp % 26 + ord('a')
            cipher += chr(tmp)
        else:
            cipher += tmp
    return cipher

flag = open('flag.txt', 'r').read()

cipher = affine(flag,?,?)

f = open('cipher.txt','w')
f.write(cipher)
f.close()