import sys, os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode
import pyzbar
import numpy as np
import cv2 as cv
import binascii

a = sys.argv[1]


if a == "-e" or a == "--encode":
    path = sys.argv[3]
    key = sys.argv[4]
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
    code.png(path, scale=10)
    image = cv.imread(path)
    image = cv.resize(image, (500, 500))
    print("Encryption Successfull")


elif a == "-ef" or a == "--encode-file":
    path = sys.argv[3]
    key = sys.argv[4]
    # Reading the public_key back in
    with open(str(key), "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    with open(sys.argv[2], 'r') as f:
        msg = bytes(f.read(), encoding='utf-8')
    encrypted = public_key.encrypt(
        msg,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    code = pyqrcode.create(binascii.hexlify(encrypted))
    code.png(path, scale=10)
    image = cv.imread(path)
    image = cv.resize(image, (500, 500))
    print("Encryption Successfull")


elif a == "-s" or a == "--scan":
    key = sys.argv[2]
    with open(str(key), "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    print("Scanning.....")
    cap = cv.VideoCapture(0)
    font = cv.FONT_HERSHEY_PLAIN
    _, frame = cap.read()
    decodedObjects = decode(frame)
    for i in decodedObjects:
        encrypted =  binascii.unhexlify(i.data.decode("utf-8"))
        if type(encrypted) == str:
            break
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


elif a == "-d" or a == "--decode":
    path = sys.argv[2]
    key = sys.argv[3]
    # Reading the private_key back in
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


elif a == "-g" or a == "--generate-keys":
    # Generating a key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
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


elif a == "-h" or a == "--help":
    print("A tool to create encrypted QR code paper backup of sensitive texts")
    print("-h, --help                 Opens the help page")
    print("-g, --generate-keys        Generate private and public keys")
    print("-e, --encode               Encode text into QR code")
    print("-ef, --encode-file         Encode text from a file into QR code")
    print("-d, --decode               Decode QR code into text")

else:
  print("Error")
