# QR Backup
The purpose of this project is to establish a more secure alternative to paper backups of sensitive texts (like passwords, crypto seeds etc.) while keeping the content of backups as interoperable as possible.

This code use `RSA SHA256` asymmetric encrption to encrypt your text and then convert it a QR code which can later be printed and kept at a safe place.

## Requirements
- Python 3
- Linux, Windows or Mac OS

## Installation
![installation](https://user-images.githubusercontent.com/59290767/128222774-cbf3601c-d85f-4d51-9f63-41d107b5127d.png)<br>
Run the following commands step by step to install QR Backup on your device.
```shell
git clone https://github.com/aayushp26/qr-backup
cd qr-backup
pip3 install -r requirements.txt
```

## Usage
### Generating Keys
![key generation](https://user-images.githubusercontent.com/59290767/128384004-b618cbdf-9c6c-49b4-ba2e-f635cff58777.png)<br>
To generate your private and public keys run the following command
```shell
python3 qr-backup.py -g
```
### Encoding Text
![encoding](https://user-images.githubusercontent.com/59290767/128384043-cf9b5990-1e6f-42a5-8f58-c14add4f14f0.png)<br>
<p align="center"><img alt="btc" src="https://user-images.githubusercontent.com/59290767/128384056-8301c68f-1091-4a44-8f81-134a1ceaaaad.png" width="30%"></p><br>
To encode text into QR code, run the following command and enter your message between " " (double quotes).
```shell
python3 qr-backup.py -e "witch collapse practice feed shame open despair creek road again ice least" qr_code.png public_key.pem
```
### Decoding Text
![decoding](https://user-images.githubusercontent.com/59290767/128384104-1a58e1d4-d33b-4ec3-a81a-1aa5b4e0fa1e.png)<br>
To decode your text from the QR code, run the following command.
```shell
python3 qr-backup.py -d code.png private_key.pem
```
## Donate
If you like this project then please consider to donate something.

| Bitcoin (BTC) | Ethereum (ETH) |
| --------- | ------------------- |
| <p align="center">bc1q32asnt6waz3czj4s8l7hvgnywpgatlvvvwwxyp</p> | <p align="center">0x311414BC8880BaEe435A59bdF7fdC632c3f6B8b1</p> |
| <p align="center"><img alt="btc" src="https://user-images.githubusercontent.com/59290767/128230575-0041db1a-c85a-438b-9374-ca5c96dda99c.jpg" width="35%"></p> | <p align="center"><img alt="eth" src="https://user-images.githubusercontent.com/59290767/128230627-0f5613b9-0f72-4d3d-9cd2-93a1ac5516e9.jpg" width="35%"></p> |
