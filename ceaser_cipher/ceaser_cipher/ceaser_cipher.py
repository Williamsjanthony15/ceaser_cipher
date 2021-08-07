import nltk
from nltk.corpus import words
nltk.download('words', quiet=True)
# nltk.download('names', quiet=True)
word_list = words.words()

# print(word_list)


# string = 'computer'
# word_count
# if string in word_list:
#     word_count +=1
#     # print(' I am here')
# else:
#     print('I am not here')\
        
#cesar cipher 

# The quick brown fox jumped over the lazy sleeping dog

# Shift of 15

# IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV

def encrypt(plain_text, key):
    encrypted_word = ''
    print(f'The plain text word is{plain_text}.')

    for i in range(len(plain_text)):
        char = plain_text[i]

        if (char.isupper()):
            encrypted_word += chr((ord(char) + key-65) % 26 + 65)
        
        else: 
            encrypted_word += chr((ord(char) + key -97) % 26 + 97)

    return encrypted_word

def decrypt(encoded, key):
    return encrypt(encoded, -key)



## This is for Encrypt method
if __name__ == "__main__":
    plain_text = 'IM gonna getCHA'
    key = 12
    print('Text is: ' + plain_text)
    print('Key is: ' + str(key))
    print('Result is: ' + encrypt(plain_text, key))
    
## This is for decrypt method
# if __name__ == "__main__":
#     print(decrypt('89', 6))