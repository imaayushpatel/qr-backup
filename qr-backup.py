import sys, os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode
import cv2 as cv
import binascii

a = sys.argv[1]
if a == "-e":
    key = sys.argv[3]
    with open(str(key), "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    msg = bytes(sys.argv[2], encoding='utf-8')
    encrypted = public_key.encrypt(
        msg,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    code = pyqrcode.create(binascii.hexlify(encrypted))
    code.png('code.png', scale=10)
    print("Encryption Successful")
elif a == "-d":
    path = sys.argv[2]
    key = sys.argv[3]
    # Reading the keys back in (for demonstration purposes)
    with open(str(key), "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    img = Image.open(path)
    result = decode(img)
    for i in result:
        encrypted =  binascii.unhexlify(i.data.decode("utf-8"))
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Decryption Successful")
    print("Decrypted Text:  ", original_message.decode('utf-8'))

elif a == "-g":
    # Generating a key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Storing the keys
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('private_key.pem', 'wb') as f:
        f.write(pem)
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('public_key.pem', 'wb') as f:
        f.write(pem)
    
    print("Keys Generation Successful")

else:
  print("Error")