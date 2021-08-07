# QR Backup
The purpose of this project is to establish a more secure alternative to paper backups of sensitive texts (like passwords, crypto seeds etc.) while keeping the content of backups as interoperable as possible.

This code use `RSA SHA256` asymmetric encryption to encrypt your text and then convert it a QR code which can later be printed and kept at a safe place.

## Requirements
- Python 3
- Linux, Windows or Mac OS

## Installation
<p align="center"><img alt="installation" src="https://user-images.githubusercontent.com/59290767/128222774-cbf3601c-d85f-4d51-9f63-41d107b5127d.png"></p><br>

Run the following commands step by step to install QR Backup on your device.

```shell
git clone https://github.com/aayushp26/qr-backup
cd qr-backup
pip3 install -r requirements.txt
```

## Usage

### Generating Keys
<p align="center"><img alt="key generation" src="https://user-images.githubusercontent.com/59290767/128384004-b618cbdf-9c6c-49b4-ba2e-f635cff58777.png"></p><br>

To generate your private and public keys, use `-g` or `--generate-keys` as give below.

```shell
python3 qr-backup.py -g
```

### Encoding Text
<p align="center"><img alt="encoding" src="https://user-images.githubusercontent.com/59290767/128384043-cf9b5990-1e6f-42a5-8f58-c14add4f14f0.png"></p><br>
<p align="center"><img alt="qr_code" src="https://user-images.githubusercontent.com/59290767/128584111-9114e0e0-98bc-441a-833c-9391323a4c08.png" width="25%"></p><br>

To encode text into QR code, use `-e` or `--encode` as given below and enter your message between " " (double quotes).

```shell
python3 qr-backup.py -e "witch collapse practice feed shame open despair creek road again ice least" qr_code.png public_key.pem
```
### Encoding Text from a File
<p align="center"><img alt="endoding_file" src="https://user-images.githubusercontent.com/59290767/128537723-56f998a0-22f1-45d2-8d53-e68ed8a6661c.png"></p><br>
<p align="center"><img alt="qr_code" src="https://user-images.githubusercontent.com/59290767/128584111-9114e0e0-98bc-441a-833c-9391323a4c08.png" width="25%"></p><br>

To encode text from a file into QR code, use `-ef` or `--encode-file` as given below.

```shell
python3 qr-backup.py -ef seed.asc qr_code.png public_key.pem
```

### Decoding QR Code
<p align="center"><img alt="decoding" src="https://user-images.githubusercontent.com/59290767/128384104-1a58e1d4-d33b-4ec3-a81a-1aa5b4e0fa1e.png"></p><br>

To decode your text from the QR code, use `-d` or `--decode` as given below.

```shell
python3 qr-backup.py -d qr_code.png private_key.pem
```

## Options

| Short| Long | Description |
|-------|----------|---------------|
| `-h` | `--help` | Opens the help page |
| `-g` | `--generate-keys` | Generate private and public keys |
| `-e` | `--encode` | Encode text into QR code |
| `-ef` | `--encode-file` | Encode text from a file into QR code |
| `-d` | `--decode` | Decode QR code into text |


## Donate
If you like this project then please consider to donate something.

| Bitcoin (BTC) | Ethereum (ETH) |
| --------- | ------------------- |
| <p align="center">bc1q32asnt6waz3czj4s8l7hvgnywpgatlvvvwwxyp</p> | <p align="center">0x311414BC8880BaEe435A59bdF7fdC632c3f6B8b1</p> |
| <p align="center"><img alt="btc" src="https://user-images.githubusercontent.com/59290767/128230575-0041db1a-c85a-438b-9374-ca5c96dda99c.jpg" width="35%"></p> | <p align="center"><img alt="eth" src="https://user-images.githubusercontent.com/59290767/128230627-0f5613b9-0f72-4d3d-9cd2-93a1ac5516e9.jpg" width="35%"></p> |
