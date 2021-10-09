import re

def func(asciiFile,ceasar_key):
    f = open(asciiFile,'r')
    text = f.read()
    textOnlyAscii=re.sub(r'[^A-Za-z ]+', '',text)
    reversed_charList =list(textOnlyAscii)[::-1] # bazoyme oloys toys xarakthres se mia lista kai thn antistrefoyme
    res = []
    for char in reversed_charList:
        if char != " " :
            if char.isupper():        # elegxoume an einai kefalaio gramma h oxi
                if ord(char)+ceasar_key>90:  # ta kefalaia sto ASCII table exoun times apo 65-90 opote an pername to Z prepei na gyrname ksana sto A
                    char = chr(64+ceasar_key-(90-ord(char)))
                else:
                    char = chr(ord(char)+ceasar_key)
            else:
                if ord(char)+ceasar_key>122:   # ta peza sto ASCII table exoun times apo 97-122 opote an pername to z prepei na gyrname ksana sto a
                    char = chr(96+ceasar_key-(122-ord(char)))
                else:
                    char = chr(ord(char)+ceasar_key)
        res.append(char) #ftiaxnoume th lista me toys telikous xaraktires
    print(''.join(res)) # me thn ''.join(res) metatrepoyme th lista sto zhtoumeno string

#func("./test.txt",10)
