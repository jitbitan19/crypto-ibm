from Crypto.Cipher import AES
import hashlib
from Crypto.Cipher.AES import MODE_GCM, MODE_CBC, MODE_CTR
from Crypto.Util.Padding import pad, unpad


MODE_ECB = 1  #: Electronic Code Book (:ref:`ecb_mode`)
MODE_CBC = 2  #: Cipher-Block Chaining (:ref:`cbc_mode`)
MODE_CFB = 3  #: Cipher Feedback (:ref:`cfb_mode`)
MODE_OFB = 5  #: Output Feedback (:ref:`ofb_mode`)
MODE_CTR = 6  #: Counter mode (:ref:`ctr_mode`)
MODE_OPENPGP = 7  #: OpenPGP mode (:ref:`openpgp_mode`)
MODE_CCM = 8  #: Counter with CBC-MAC (:ref:`ccm_mode`)
MODE_EAX = 9  #: :ref:`eax_mode`
MODE_SIV = 10  #: Synthetic Initialization Vector (:ref:`siv_mode`)
MODE_GCM = 11  #: Galois Counter Mode (:ref:`gcm_mode`)
MODE_OCB = 12  #: Offset Code Book (:ref:`ocb_mode`)


def aes_enc(
    msg: str,
    passphrase: str,
    hashfn: str,
    ciphermode: str,
) -> tuple[str, str, str]:
    """
    An AES Encryptor.
    # Parameters:
        `msg`: Message to be encrypted
        `passphrase`: An encryption key (use a key from any KDF)
        `hashfn`: Hasher of the given key `(sha512_224, sha3_512, sha3_384, ripemd160, sha3_224, sha256, blake2b, blake2s, sha512_256, sha224, sha384, sha512, sha3_256)`
        `ciphermode`: AES cipher modes, `(GCM, CBC, CTR)`
    # Returns:
        Tuple consisting of hex of `(ciphertext, nonce/iv, auth_tag)`
    """
    hasher = hashlib.new(hashfn)
    hasher.update(passphrase.encode())
    key = hasher.digest()
    auth_tag = b"0"
    iv = b"0"
    if ciphermode == "GCM":
        cipher = AES.new(key, MODE_GCM)
        ct, auth_tag = cipher.encrypt_and_digest(msg.encode())
        iv = cipher.nonce
    if ciphermode == "CBC":
        cipher = AES.new(key, MODE_CBC)
        ct = cipher.encrypt(pad(msg.encode(), AES.block_size, style="pkcs7"))
        iv = cipher.iv
    if ciphermode == "CTR":
        cipher = AES.new(key, MODE_CTR)
        ct = cipher.encrypt(msg.encode())
        iv = cipher.nonce

    return (ct.hex(), iv.hex(), auth_tag.hex())


def aes_dec(
    cipher: tuple[str, str, str],
    passphrase: str,
    hashfn: str,
    ciphermode: str,
) -> tuple[str, int | None]:
    """
    An AES Decryptor
    # Parameters:
        `cipher`: Hex of cipher text
        `passphrase`: Key used for encryption
        `hashfn`: Hasher of the given key `(sha512_224, sha3_512, sha3_384, ripemd160, sha3_224, sha256, blake2b, blake2s, sha512_256, sha224, sha384, sha512, sha3_256)`
        `ciphermode`: AES cipher modes, `(GCM, CBC, CTR)`
    # Returns:
        Tuple of [plaintext, tag_validity(only for GCM)]
    """
    hasher = hashlib.new(hashfn)
    hasher.update(passphrase.encode())
    ct, iv, auth_tag = cipher
    key = hasher.digest()
    tag = None

    if ciphermode == "GCM":
        dec = AES.new(key, MODE_GCM, bytes.fromhex(iv))
        pt = dec.decrypt(bytes.fromhex(ct))
        try:
            dec.verify(bytes.fromhex(auth_tag))
            tag = 1
        except:
            tag = 0
    if ciphermode == "CBC":
        dec = AES.new(key, MODE_CBC, bytes.fromhex(iv))
        pt = dec.decrypt(bytes.fromhex(ct))
    if ciphermode == "CTR":
        dec = AES.new(key, MODE_CTR, bytes.fromhex(iv))
        pt = dec.decrypt(bytes.fromhex(ct))
    try:
        return (pt.decode(), tag)
    except:
        return (pt.hex(), tag)
