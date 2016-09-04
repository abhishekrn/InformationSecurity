##for caeser encryption
##python classical_encryption.py caeser e input_file_name shift
##for caeser decryption
##python classical_encryption.py caeser d input_file_name shift


import sys

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

if __name__ == "__main__":
    encryption_tech = sys.argv[1]
    what = sys.argv[2]
    fi = open(sys.argv[3], "r")
    fo = open("output.txt", "w")
    if encryption_tech == "caeser":
        if what == "e":
            output = caeser_encrypt(fi.read(), int(sys.argv[4]))
        if what == "d":
            output = caeser_decrypt(fi.read(), int(sys.argv[4]))
        fo.write(output)
    fi.close()
    fo.close()
