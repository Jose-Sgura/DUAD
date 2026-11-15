import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_keys(path = "keys"):
    os.makedirs(path, exist_ok=True)

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format= serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    private_path = os.path.join(path, "private.pem")
    public_path = os.path.join(path, "public.pem")

    with open(private_path, "wb") as f:
        f.write(private_pem)

    with open(public_path, "wb") as f:
        f.write(public_pem)
    print(f"Generated keys:\n {private_path}\n {public_path}")  

if __name__=="__main__":
    generate_keys()