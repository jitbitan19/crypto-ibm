from Crypto.PublicKey import ECC
from Signature import eddsa
from Crypto.Hash import SHA512

message = b'I give my permission to order #4355'
prehashed_message = SHA512.new(message)
key = ECC.import_key(open("private_ed25519.pem").read())
signer = eddsa.new(key, 'rfc8032')
signature = signer.sign(prehashed_message)