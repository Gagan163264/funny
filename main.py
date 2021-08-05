import binascii
import sys

if(len(sys.argv)==1):
    sys.exit("No filename specified")

filename = sys.argv[1]
if(filename[-3:]!='mp4'):
    exitstr = filename[-3:]+' not supported'
    sys.exit(exitstr)

f = open(filename, 'rb')
fr = open(filename[:-4]+'C.mp4', 'wb')
content = f.read()
str = binascii.hexlify(content)
index = str.find('6d766864'.encode())+8+24
str = str[:index]+'000000017fffffff'.encode()+str[index+16:]
fr.write(binascii.unhexlify(str))
