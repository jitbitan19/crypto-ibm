from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

message = 'To be signed'
key = RSA.import_key(open('privkey.der').read())
h = SHA256.new(message)
signature = pss.new(key).sign(h)