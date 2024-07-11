from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from crypto_module.mycipher import MyCipher
from crypto_module.utils import generate_key, write_key_to_file, read_key_from_file
import base64
class AESCipher:
    def encrypt(self, data):
        # Generate and save the key
        key = generate_key()
        key_file = 'aes_key.bin'
        write_key_to_file(key, key_file)
        # Read the key from file
        key = read_key_from_file(key_file)
        objMyCipher = MyCipher(key)
        cipher = objMyCipher.getCipher()
        # Create an instance of AESCipher
        #cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv, ct
    """ def decrypt(self, iv, ct):
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8') """