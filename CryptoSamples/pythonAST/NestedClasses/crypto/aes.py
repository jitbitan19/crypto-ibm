from Crypto.Cipher import AES
from Crypto import Random

class MyCrypto:
    def generateKey():
        key = b'Sixteen byte key'
        return key
    
    def generateIV():
        iv = Random.new().read(AES.block_size)
        return iv

    def encrypt(key,iv,data): # type: ignore
        cipher = AES.new(key, AES.MODE_CFB, iv) # type: ignore
        msg = iv + cipher.encrypt(data)
        return msg
    
def myfunction():
    print("myfunction")