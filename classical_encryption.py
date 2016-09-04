##for caeser encryption (shift is a number)
##python classical_encryption.py caeser e input_file_name shift
##for caeser decryption
##python classical_encryption.py caeser d input_file_name shift



##for autokey encryption
##python classical_encryption.py autokey e message key
##for autokey decryption
##python classical_encryption.py autokey d encrypted_message key



import sys
def shift(l , n):
    return l[n:] + l[:n]

def caeser_encrypt(message, shift):
    encrypted_message = []
    for i  in message:
        if i.isalpha() == True:
            encrypted_message.append(chr(ord('a') + ((ord(i) - ord('a') + shift) % 26)))
        else:
            encrypted_message.append(i)
    return "".join(encrypted_message)



def caeser_decrypt(message, shift):
    decrypted_message = []
    for i  in message:
        if i.isalpha() == True:
            decrypted_message.append(chr(ord('a') + ((ord(i) - ord('a') - shift) % 26)))
        else:
            decrypted_message.append(i)
    return "".join(decrypted_message)


def autokey_encrypt(message, key):
    lis = range(0, 26)
    addendum = list(key) + list(message)[:len(message) - len(key)]
    table = []
    for i in xrange(26):
        table.append(shift(lis,i))
    i = 0
    encrypted_message = []
    while i < len(message):
        b = message[i]
        a = addendum[i]
        encrypted_message.append(chr(ord('a') + (table[ord(a) - ord('a')][ord(b) - ord('a')])))
        i += 1
    return "".join(encrypted_message)
    
 
def autokey_decrypt(message, key):
    lis = range(0, 26)
    addendum = list(key)
    table = []
    for i in xrange(26):
        table.append(shift(lis,i))
    i = 0
    decrypted_message = []
    while i < len(message):
        b = message[i]
        a = addendum[i]
        decrypted_message.append(chr(ord('a') + (table[ord(a) - ord('a')].index(ord(b) - ord('a')))))
        addendum.append(decrypted_message[i])
        i += 1
    return "".join(decrypted_message)
        

if __name__ == "__main__":
    encryption_tech = sys.argv[1]
    what = sys.argv[2]
    if encryption_tech == "caeser":
        fi = open(sys.argv[3], "r")
        fo = open("output.txt", "w")
        if what == "e":
            output = caeser_encrypt(fi.read(), int(sys.argv[4]))
        if what == "d":
            output = caeser_decrypt(fi.read(), int(sys.argv[4]))
        fo.write(output)
        fi.close()
        fo.close()
    if encryption_tech == "autokey":
        if what == "e":
	    print autokey_encrypt(sys.argv[3], sys.argv[4])
        if what == "d":
	    print autokey_decrypt(sys.argv[3], sys.argv[4])









##print autokey_encrypt("defendtheeastwallofthecastle", "fortification")
##print autokey_decrypt(autokey_encrypt("defendtheeastwallofthecastle", "fortification"), 'fortification')
