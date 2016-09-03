##To encrypt run:
##python steno.py imagetohide.png e message outputimage


##To decrypt run:
##python steno.py outputimage.png d lengthofimage


import Image
import sys
def wordtopixel(string):
    a = ord(string)  
    b = 0
    c = 0
    return (a, b, c)

def pixeltoword(pixel):
    return chr((pixel[0]))


def encrypt(picture, width, height, message):
    i = 0
    for x in range(0, width):
        for y in xrange(0, height, 10):
            if i == len(message):
                return
            else:
                picture.putpixel((x, y), wordtopixel(message[i]))
                i += 1

def decrypt(picture, width, height, length):
    i = 0
    lis = []
    for x in range(0, width):
        for y in xrange(0, height, 10):
            if i == length:
                return "".join(lis)
            else:
                lis.append(pixeltoword(picture.getpixel((x, y))))
                i += 1


if __name__ == "__main__":
    picture = Image.open(sys.argv[1])
    width, height = picture.size
    what = sys.argv[2]
    if what == 'e':
        message = sys.argv[3]
        print "Encrypting...."
        encrypt(picture, width, height, message)
        print "message of length: " + str(len(message)) + " saved at "  + sys.argv[4] + ".png"
        picture.save(sys.argv[4] + ".png")
    if what == 'd':
        print "Decrypting...."
        length = int(sys.argv[3])
        print decrypt(picture, width, height, length)
