import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

#CBC with Fix IV

data = 'I love Medium'
key = 'AAAAAAAAAAAAAAAA' #16 char for AES128

#FIX IV
iv =  'BBBBBBBBBBBBBBBB'.encode('utf-8') #16 char for AES128

def encrypt(data,key,iv):
        data= pad(data.encode(),16)
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
        return base64.b64encode(cipher.encrypt(data))

def decrypt(enc,key,iv):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc),16)

encrypted = encrypt(data,key,iv)
print('encrypted CBC base64 : ',encrypted.decode("utf-8", "ignore"))

decrypted = decrypt(encrypted,key,iv)
print('data: ', decrypted.decode("utf-8", "ignore"))