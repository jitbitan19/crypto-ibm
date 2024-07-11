from Crypto.Cipher import AES
class MyCipher:
    def __init__(self, key):
        self.key = key
    def getCipher(self):
        return  AES.new(self.key, AES.MODE_CBC)