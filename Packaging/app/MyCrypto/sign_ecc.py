from Crypto.PublicKey import ECC
from Crypto.Hash import SHA3_256
from Crypto.Signature import DSS


def gen_ecc_sign_key(key_name: str, curve: str = "p256"):
    """
    A key pair generator for ECC signing
    # Parameters:
        `key_name`: a  name for referencing the keys
        `curve`: curve used for key generation `p192, p224, p256, p384, p521, ed25519, ed448`
    # Actions:
        Creates an ECC key pair (public key, private key)
    """
    key_pair = ECC.generate(curve=curve)
    pub_key = key_pair.public_key()

    with open(f"{key_name}__ecc_pvt_key.pem", "wt") as f:
        f.write(key_pair.export_key(format="PEM"))
    with open(f"{key_name}__ecc_pub_key.pem", "wt") as f:
        f.write(pub_key.export_key(format="PEM"))


def ecc_sign(msg: str, key_name: str) -> str:
    """
    An ECC signer
    # Parameters:
        `msg`: message to be signed
        `key_name`: reference to the private key({key_name}__ecc_pvt_key.pem)
    # Returns:
        Signature in hex
    """
    with open(f"{key_name}__ecc_pvt_key.pem", "rt") as f:
        key = ECC.import_key(f.read())
    signer = DSS.new(key=key, mode="fips-186-3")
    return signer.sign(SHA3_256.new(msg.encode())).hex()
.

def ecc_verify(msg: str, sign: str, key_name: str) -> bool:
    """
    An ECC validator
    # Parameters:
        `msg`: signed message
        `sign`: signature (in hex)
        `key_name`: reference to the public key ({key_name}__ecc_pub_key.pem})
    # Returns:
        Validity of the signature and the message
    """
    with open(f"{key_name}__ecc_pub_key.pem", "rt") as f:
        key = ECC.import_key(f.read())
    validator = DSS.new(key=key, mode="fips-186-3")
    try:
        return validator.verify(SHA3_256.new(msg.encode()), bytes.fromhex(sign))
    except:
        return False
