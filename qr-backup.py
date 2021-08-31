import sys
import os
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import cv2 as cv
import numpy as np
from PIL import Image
import pyqrcode
from pyzbar.pyzbar import decode
import pyzbar

option = sys.argv[1]

if option == "-e" or option == "--encode":
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

elif option == "-ef" or option == "--encode-file":
    path = sys.argv[3]
    key = sys.argv[4]
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

elif option == "-s" or option == "--scan":
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
        encrypted = binascii.unhexlify(i.data.decode("utf-8"))
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

elif option == "-d" or option == "--decode":
    path = sys.argv[2]
    key = sys.argv[3]
    with open(str(key), "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    img = Image.open(path)
    result = decode(img)
    for i in result:
        encrypted = binascii.unhexlify(i.data.decode("utf-8"))
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

elif option == "-g" or option == "--generate-keys":
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    public_key = private_key.public_key()
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

elif option == "-h" or option == "--help":
    print("A tool to create encrypted QR code paper backup of sensitive texts")
    print("-h, --help                 Opens the help page")
    print("-g, --generate-keys        Generate private and public keys")
    print("-e, --encode               Encode text into QR code")
    print("-ef, --encode-file         Encode text from a file into QR code")
    print("-s, --scan                 Scan the QR code from printed format")
    print("-d, --decode               Decode QR code into text")

else:
    print("Error")
