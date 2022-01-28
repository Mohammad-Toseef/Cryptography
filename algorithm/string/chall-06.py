import binascii
hexpair = '526576657273696e672e4944'
encoded = binascii.unhexlify(hexpair)
C = 0x54
decoded = ''.join(chr(b ^ C) for b in encoded)

if decoded.isprintable():
        print(C, decoded)
