from MyCrypto.hash import hash

message = "Hashing Testing"
hash_digest = hash(message, "SHA3_256")

print(f"Message: {message}")
print(f"Hash Digest: {hash_digest}")
