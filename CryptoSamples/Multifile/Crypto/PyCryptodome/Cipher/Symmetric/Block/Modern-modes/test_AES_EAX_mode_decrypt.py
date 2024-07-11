import json
from base64 import b64decode
from Crypto.Cipher import AES

# We assume that the key was securely shared beforehand
try:
    b64 = json.loads(json_input)
    json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
    jv = {k:b64decode(b64[k]) for k in json_k}

    cipher = AES.new(key, AES.MODE_EAX, nonce=jv['nonce'])
    cipher.update(jv['header'])
    plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
    print("The message was: " + plaintext.decode('utf-8'))
except (ValueError, KeyError):
    print("Incorrect decryption")