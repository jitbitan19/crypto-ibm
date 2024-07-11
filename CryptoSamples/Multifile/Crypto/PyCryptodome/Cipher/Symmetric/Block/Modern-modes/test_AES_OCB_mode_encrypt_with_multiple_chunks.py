import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

header = b'header'
data = [b'chunk1', b'chunk2', b'chunk3']
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_OCB)
cipher.update(header)
ciphertext = b''
for chunk in data:
    ciphertext += cipher.encrypt(chunk)
ciphertext += cipher.encrypt()
tag = cipher.digest()

json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
json_v = [ b64encode(x).decode('utf-8') for x in (cipher.nonce, header, ciphertext, tag) ]
result = json.dumps(dict(zip(json_k, json_v)))
print(result)