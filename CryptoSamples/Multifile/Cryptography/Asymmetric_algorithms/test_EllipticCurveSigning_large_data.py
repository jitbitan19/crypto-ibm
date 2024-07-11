from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils

chosen_hash = hashes.SHA256()
hasher = hashes.Hash(chosen_hash)
hasher.update(b"data & ")
hasher.update(b"more data")
digest = hasher.finalize()
sig = private_key.sign(
    digest,
    ec.ECDSA(utils.Prehashed(chosen_hash))
)
public_key = private_key.public_key()
public_key.verify(
    sig,
    digest,
    ec.ECDSA(utils.Prehashed(chosen_hash))
)