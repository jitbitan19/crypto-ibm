from cryptography.hazmat.primitives import hashes
digest1 = hashes.Hash(hashes.SHA3_224())
digest1.update(b"abc")
digest1.update(b"123")
digest1.finalize()

digest2 = hashes.Hash(hashes.SHA3_256())
digest2.update(b"abc")
digest2.update(b"123")
digest2.finalize()

digest3 = hashes.Hash(hashes.SHA3_384())
digest3.update(b"abc")
digest3.update(b"123")
digest3.finalize()

digest4 = hashes.Hash(hashes.SHA3_512())
digest4.update(b"abc")
digest4.update(b"123")
digest4.finalize()
