import json
from base64 import b64decode
from Crypto.Cipher import AES

# We assume that the key was securely shared beforehand
try:
    b64 = json.loads(json_input)
    nonce = b64decode(b64['nonce'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    pt = cipher.decrypt(ct)
    print("The message was: ", pt)
except (ValueError, KeyError):
    print("Incorrect decryption")