import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

#CBC mode with random IV

data = 'I love Medium'
key = 'AAAAAAAAAAAAAAAA' #16 char for AES128

#Random IV more secure
iv =  get_random_bytes(16) #16 char for AES128

def encrypt(data,key,iv):
        data = pad(data.encode(),16)
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
        print('random IV : ' , base64.b64encode(cipher.iv).decode('utf-8'))
        return base64.b64encode(cipher.encrypt(data)),base64.b64encode(cipher.iv).decode('utf-8')
  
def decrypt(enc,key,iv):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, base64.b64decode(iv))
        return unpad(cipher.decrypt(enc),16)

encrypted, iv = encrypt(data,key,iv)
print('encrypted CBC base64 : ',encrypted.decode("utf-8", "ignore"))

decrypted = decrypt(encrypted,key,iv)
print('data: ', decrypted.decode("utf-8", "ignore"))