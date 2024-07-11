import json
from base64 import b64decode
from Crypto.Cipher import AES

# We assume that the key was securely shared beforehand
try:
    b64 = json.loads(json_input)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    pt = cipher.decrypt(ct)
    print("The message was: ", pt)
except (ValueError, KeyError):
    print("Incorrect decryption")