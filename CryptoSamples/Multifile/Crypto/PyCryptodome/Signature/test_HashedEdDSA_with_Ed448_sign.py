from Crypto.PublicKey import ECC
from Signature import eddsa
from Crypto.Hash import SHAKE256

message = b'I give my permission to order #4355'
prehashed_message = SHAKE256.new(message)
key = ECC.import_key(open("private_ed448.pem").read())
signer = eddsa.new(key, 'rfc8032')
signature = signer.sign(prehashed_message)