from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

plaintext = input('Data:')
key = bytes(input('Key:'),'utf-8')
iv = bytes(input('IV:'),'utf-8')
obj = AES.new(key, AES.MODE_CBC,iv) #Insertamos configuración al AES
mode = input("Cifrar (c) o descifrar (d):\n")

if(mode == 'c'): #ciframos
    plaintext = bytes(plaintext,'utf-8')
    result = obj.encrypt(pad(plaintext,AES.block_size))
    print(result.hex())

elif(mode == 'd'): #desciframos
    plaintext = binascii.unhexlify(plaintext)
    result =obj.decrypt(plaintext)
    print(result.decode('utf-8'))