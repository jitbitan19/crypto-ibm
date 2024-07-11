import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHMAC

salt = os.urandom(16)
otherinfo = b"concatkdf-example"
ckdf = ConcatKDFHMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    otherinfo=otherinfo,
)
key = ckdf.derive(b"input key")
ckdf = ConcatKDFHMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    otherinfo=otherinfo,
)
ckdf.verify(b"input key", key)