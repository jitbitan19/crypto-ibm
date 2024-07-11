from Crypto.Hash import keccak

keccak_hash = keccak.new(digest_bits=512)
keccak_hash.update(b'Some data')
print(keccak_hash.hexdigest())