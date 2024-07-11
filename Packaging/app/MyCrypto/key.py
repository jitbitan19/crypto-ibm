from Crypto.Protocol.KDF import PBKDF2, scrypt
from Crypto.Hash import (
    BLAKE2b,
    BLAKE2s,
    RIPEMD160,
    SHA224,
    SHA256,
    SHA384,
    SHA3_224,
    SHA3_256,
    SHA3_384,
    SHA3_512,
    SHA512,
    keccak,
)
from Crypto.Random import get_random_bytes

all_hash = [
    BLAKE2b,
    BLAKE2s,
    RIPEMD160,
    SHA224,
    SHA256,
    SHA384,
    SHA3_224,
    SHA3_256,
    SHA3_384,
    SHA3_512,
    SHA512,
    keccak,
]


def key_gen(
    pwd: str,
    method: str,
    hashfn: str,
    salt_len: int,
    key_len: int,
    iter: int = (1 << 10),
) -> str:
    """
    A hash based key derivator with random salt
    # Parameters:
        `pwd`: password to be hashed
        `method`: key drivation fucntion (`PBKDF2` or `scrypt`)
        `hashfn`: hash function required (`SHA224 SHA256 SHA384 SHA512 SHA3_224 SHA3_256 SHA3_384 SHA3_512 BLAKE2 BLAKE2s BLAKE2b`)
        `salt_len`: length of random salt, (in `bytes`)
        `key_len`: length of output key, (in `bytes`)
    """
    hasher = None
    for i in all_hash:
        if i.__name__ == f"Crypto.Hash.{hashfn}":
            hasher = i
    salt_ = get_random_bytes(salt_len)
    if method == "PBKDF2":
        key = PBKDF2(
            password=pwd,
            salt=salt_,
            dkLen=64,
            count=iter,
            hmac_hash_module=hasher,
        )
    else:
        key = scrypt(
            password=pwd,
            salt=salt_.hex(),
            key_len=key_len,
            N=iter,
            r=8,
            p=1,
        )
    return key.hex()  # type: ignore
