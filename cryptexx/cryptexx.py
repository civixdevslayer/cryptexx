from random import randint

def encrypt(text):
    tmp = 0
    encypted_text = ""
    
    for i in range(len(text)):
        if tmp == 0:
            encypted_text = encypted_text + chr(randint(33, 126))
            encypted_text = encypted_text + chr(ord(text[i]) + 1)
            
            tmp = tmp + 1
        else:
            encypted_text = encypted_text + chr(ord(text[i]) + 1)
            tmp = tmp - 1
    return encypted_text

def decrypt(encypted_text):
    tmp = 0
    decrypted_text = ""

    for i in range(len(encypted_text)):
        if tmp == 0:
            tmp = tmp + 2
        else:
            decrypted_text = decrypted_text + chr(ord(encypted_text[i]) - 1)
            tmp = tmp - 1
    return decrypted_text
            