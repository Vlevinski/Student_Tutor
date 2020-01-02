alphabet = 'abcdefghijklmnopqrstuvwxyz'

def shift_by_n(n, value):
    as_bytes = value.encode('utf8')
    encoded = []
    for v in as_bytes:
        if 97 <= v <= 122:
            v = ((v - 97 + n) % 26) + 97
        encoded.append(v)
    return bytes(encoded).decode('utf8')

def encode(shift, string):
    return shift_by_n(shift, string)

def decode(shift, string):
    return shift_by_n(-shift, string)

a="Hello World Java Python"
print (a)
ae = encode(13, a)
print(ae)
print(decode(13, ae))
