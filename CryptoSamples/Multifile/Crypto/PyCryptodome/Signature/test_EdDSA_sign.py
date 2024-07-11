from Crypto.PublicKey import ECC
from Signature import eddsa

message = b'I give my permission to order #4355'
key = ECC.import_key(open("private_ed25519.pem").read())
signer = eddsa.new(key, 'rfc8032')
signature = signer.sign(message)