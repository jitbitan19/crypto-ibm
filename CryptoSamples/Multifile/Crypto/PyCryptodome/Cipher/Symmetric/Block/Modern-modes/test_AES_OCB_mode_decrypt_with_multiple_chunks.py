import json
from base64 import b64decode
from Crypto.Cipher import AES

# We assume that the key was securely shared beforehand
try:
    b64 = json.loads(json_input)
    json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
    jv = {k:b64decode(b64[k]) for k in json_k}

    cipher = AES.new(key, AES.MODE_OCB, nonce=jv['nonce'])
    cipher.update(jv['header'])
    ciphertext = jv['ciphertext']

    # Split into small chunks, just for demo purposes
    chunks = [ ciphertext[i:i+2] for i in range(0, len(ciphertext), 2) ]

    plaintext = b''
    for chunk in chunks:
        plaintext += cipher.decrypt(chunk)
    plaintext += cipher.decrypt()
    cipher.verify(jv['tag'])

    print("The message was: " + plaintext.decode('utf-8'))
except (ValueError, KeyError):
    print("Incorrect decryption")