import base64

def Caesar(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch.islower():
            ciphertext += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        elif ch.isupper():
            ciphertext += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        else:
            ciphertext += ch
    return ciphertext


flag = open('flag.txt', 'r').read()

cipher = base64.b64encode(Caesar(flag, ?).encode()).decode()

f = open('cipher.txt','w')
f.write(cipher)
f.close()