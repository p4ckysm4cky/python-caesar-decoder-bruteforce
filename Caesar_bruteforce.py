def cipherInput():
    global plainText
    print("Welcome to the Caesar Cipher")
    plainText = input("Please enter the text you would like to decrypt\n:").lower()

def bruteOutput():
    decryptedText = []
    key = 1
    while key < 26:
        for i in plainText:
            if ord(i) > 96 and ord(i) < 123:
                ordinal = ord(i) - key
                if ordinal < 97:
                    ordinal = 123 - (97 - ordinal)
            else:
                ordinal = ord(i)
            
            letter = chr(ordinal)

            
            decryptedText.append(letter)
        decryptNorm = ''.join(decryptedText)
        print("%d: %s \n" %(key,decryptNorm))
        key +=1
        decryptedText = []

cipherInput()
bruteOutput()