#matrix class
class matrix:
    def __init__(self, rows):
        self.rows = rows
    def item(self, posx, posy):
        return(self.rows[int(posx)][int(posy)])
    def find(self, l):
        for a in range(len(self.rows)):
            for b in range(len(self.rows[0])):
                if l == self.rows[a][b]:
                    return([a, b])
            
#what happens here is that first we have matrix 4 by 7 with all the letters of the alphabet and a space and a dot.
#then we find the colum and row of each submited letter and save that as encode.
#then we make a key matrix and then we take each letter from encode and switch it with the corresponding letter in the key.
#then we get our newtext!
def encode():        
    square = matrix([['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','P'], ['Q','R','S','T'],['U','V','W','X'],['Y','Z',' ','.']])
    encode = []
    text = input('your text to encode: ')
    text = text.upper()
    for x in range(len(text)):
                    encode.append(square.find(text[x]))
    print(encode)                
    #now to make the key matrix
    key = input('your key the longer the better: ')
    key = key.upper()
    kmat = []
    for x in range(len(key)):
        kmat.append(key[x])
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','.']
    x = 0
    while x != 28:
        a = alphabet[x]
        if a not in kmat:
            kmat.append(a)
        else:
            pass
        x += 1
    l1 = kmat[0:4]
    l2 = kmat[4:8]
    l3 = kmat[8:12]
    l4 = kmat[12:16]
    l5 = kmat[16:20]
    l6 = kmat[20:24]
    l7 = kmat[24:28]
    kmat = [l1,l2,l3,l4,l5,l6,l7]

    keymat = matrix(kmat)
    newtext = ''
    for x in range(len(text)):
        newtext = str(keymat.item(encode[x][0], encode[x][1]))+newtext
    newtext = newtext.lower()       
    print(newtext)    
    
                

#this decode function is basicly the encode one backwards

def decode():
    #now to make the key matrix
    key = input('your key: ')
    key = key.upper()
    kmat = []
    for x in range(len(key)):
        kmat.append(key[x])
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','.']
    x = 0
    while x != 28:
        a = alphabet[x]
        if a not in kmat:
            kmat.append(a)
        else:
            pass
        x += 1
        
    l1 = kmat[0:4]
    l2 = kmat[4:8]
    l3 = kmat[8:12]
    l4 = kmat[12:16]
    l5 = kmat[16:20]
    l6 = kmat[20:24]
    l7 = kmat[24:28]
    kmat = [l1,l2,l3,l4,l5,l6,l7]
 
    square = matrix(kmat)
    encode = []
    text = input('your text to decode: ')
    text = text.upper()
    for x in range(len(text)):
                    encode.append(square.find(text[x]))   

    keymat = matrix([['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','P'], ['Q','R','S','T'],['U','V','W','X'],['Y','Z',' ','.']])
    newtext = ''
    for x in range(len(text)):
        newtext = str(keymat.item(encode[x][0], encode[x][1]))+newtext
    newtext = newtext.lower()    
    print(newtext)

encode()
print('\n now if youd like to decode \n')
decode()

#I know I could make this code a lot but it looks nicer like this
