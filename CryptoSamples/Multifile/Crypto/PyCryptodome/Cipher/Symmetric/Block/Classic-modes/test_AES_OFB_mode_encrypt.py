import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"secret"
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_OFB)
ct_bytes = cipher.encrypt(data)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv':iv, 'ciphertext':ct})
print(result)