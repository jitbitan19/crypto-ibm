from Crypto.Hash import (
    BLAKE2b,
    BLAKE2s,
    RIPEMD160,
    SHA224,
    SHA256,
    SHA384,
    SHA512,
    SHA3_224,
    SHA3_256,
    SHA3_384,
    SHA3_512,
    SHA512,
    keccak,
)

all_hash = [
    BLAKE2b,
    BLAKE2s,
    RIPEMD160,
    SHA224,
    SHA256,
    SHA384,
    SHA512,
    SHA3_224,
    SHA3_256,
    SHA3_384,
    SHA3_512,
    SHA512,
    keccak,
]


def hash(msg: str, method: str = "SHA3_256") -> str:
    """
    Computes the hash digest of the given msg.

    # Parameters:
        `msg` : Plain Text
        `method` : `SHA224 SHA256 SHA384 SHA512 SHA3_224 SHA3_256 SHA3_384 SHA3_512 BLAKE2 BLAKE2s BLAKE2b`
    # Returns:
        `hexdigest`: Cipher Text, a string consisting of the hex codeo of the hash digest

    """

    for i in all_hash:
        if i.__name__ == f"Crypto.Hash.{method}":
            if method == "keccak":
                hasher = i.new(digest_bits=512)
            else:
                hasher = i.new()

    hasher.update(msg.encode())
    return hasher.hexdigest()
