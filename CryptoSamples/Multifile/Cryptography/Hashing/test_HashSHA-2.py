from cryptography.hazmat.primitives import hashes

digest0 = hashes.Hash(hashes.SHA224())
digest0.update(b"abc")
digest0.update(b"123")
digest0.finalize()

digest1 = hashes.Hash(hashes.SHA256())
digest1.update(b"abc")
digest1.update(b"123")
digest1.finalize()

digest2 = hashes.Hash(hashes.SHA384())
digest2.update(b"abc")
digest2.update(b"123")
digest2.finalize()

digest3 = hashes.Hash(hashes.SHA512())
digest3.update(b"abc")
digest3.update(b"123")
digest3.finalize()

digest4 = hashes.Hash(hashes.SHA512_224())
digest4.update(b"abc")
digest4.update(b"123")
digest4.finalize()

digest5 = hashes.Hash(hashes.SHA512_256())
digest5.update(b"abc")
digest5.update(b"123")
digest5.finalize()