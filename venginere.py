alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def switch(n,k):
    num = (alphabet.index(n)+alphabet.index(k))%26
    n = alphabet[num]
    return n

def swatch(n,k):
    num = (alphabet.index(n)-alphabet.index(k))%26
    n = alphabet[num]
    return n

def trunc(s,l):
    if l > 0:
        return s[:l] + trunc(s, l - len(s))
    return ''

def en(text, key):
    key = trunc(key, len(text))
    n = list(text)
    k = list(key)
    for x in range(len(text)):
        n[x] = switch(n[x], k[x])
    n = "".join(n)    
    return(n)

def de(text, key):
    key = trunc(key, len(text))
    n = list(text)
    k = list(key)
    for x in range(len(text)):
        n[x] = swatch(n[x], k[x])
    n = "".join(n)    
    return(n)

def encode():
    text = input('your text to encode ')
    text = text.upper()
    key = input('your key ')
    key = key.upper()
    words = text.split()
    result = []
    for x in range(len(words)):
        result.append(en(words[x],key))
    result = " ".join(result)
    return(result)

def decode():
    text = input('your text to decode ')
    text = text.upper()
    key = input('your key ')
    key = key.upper()
    words = text.split()
    result = []
    for x in range(len(words)):
        result.append(de(words[x],key))
    result = " ".join(result)
    return(result)

forever = 0
while forever != 1:
    what = input('encode or decode? (e, d) ')
    if what == 'e':
        print(encode())
    elif what == 'd':
        print(decode())
    else:
        print('sorry only d or e')

        

