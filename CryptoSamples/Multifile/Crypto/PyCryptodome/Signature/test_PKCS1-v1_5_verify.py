from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

key = RSA.import_key(open('public_key.der').read())
h = SHA256.new(message)
try:
    pkcs1_15.new(key).verify(h, signature)
    print("The signature is valid.")
except (ValueError, TypeError):
   print("The signature is not valid.")