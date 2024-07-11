from Crypto.PublicKey import ECC
from Signature import eddsa

message = b'I give my permission to order #4355'
key = ECC.import_key(open("public_ed25519.pem").read())
verifier = eddsa.new(key, 'rfc8032')
try:
    verifier.verify(message, signature)
    print("The message is authentic")
except ValueError:
    print("The message is not authentic")