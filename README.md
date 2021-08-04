# QR Backup
The purpose of this project is to establish a more secure alternative to paper backups of sensitive texts (like passwords, crypto seeds etc.) while keeping the content of backups as interoperable as possible.

This code use `RSA SHA256` asymmetric encrption to encrypt your text and then convert it a QR code which can later be printed and kept at a safe place.

## Requirements
- Python 3
- Linux, Windows or Mac OS

## Installation
![installation](https://user-images.githubusercontent.com/59290767/128222774-cbf3601c-d85f-4d51-9f63-41d107b5127d.png)
Run the following commands step by step to install QR Backup on your device.
```shell
git clone https://github.com/aayushp26/qr-backup
cd qr-backup
pip3 install -r requirements.txt
```

## Usage
![usage](https://user-images.githubusercontent.com/59290767/128222817-c8d785e7-b985-4a1f-ad0f-ad65155b2e80.png)
### Generating Keys
To generate your private and public keys run the following command
```shell
python3 qr-backup.py -g
```
### Encoding Text
To encode text into QR code, run the following command and enter your message between " " (double quotes).
```shell
python3 qr-backup.py -e "witch collapse practice feed shame open despair creek road again ice least" public_key.pem
```
### Decoding Text
To decode your text from the QR code, run the following command.
```shell
python3 qr-backup.py -d code.png private_key.pem
```
## Donate
If you like this project then please consider to donate something.
- Bitcoin - 
- Ethereum - 
