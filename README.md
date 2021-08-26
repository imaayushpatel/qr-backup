# QR Backup
The purpose of this project is to establish a more secure alternative to paper backups of sensitive texts (like passwords, crypto seeds etc.) while keeping the content of backups as interoperable as possible.

This code use `RSA SHA256` asymmetric encryption to encrypt your text and then convert it a QR code which can later be printed and kept at a safe place.

## Installation
<p align="center"><img alt="installation" src="https://user-images.githubusercontent.com/59290767/129384671-e98580f1-d8d8-4842-a3cf-22cdc92c1026.png"></p><br>

Run the following commands step by step to install QR Backup on your device.

```shell
git clone https://github.com/iamaayushp/qr-backup.git
cd qr-backup
pip3 install -r requirements.txt
```

## Usage

### Generating Keys
<p align="center"><img alt="key generation" src="https://user-images.githubusercontent.com/59290767/129384914-47fa1c06-c878-4b96-a3b3-6e74e7c37826.png"></p><br>

To generate your private and public keys, use `-g` or `--generate-keys` as give below.

```shell
python3 qr-backup.py -g
```

### Encoding Text
<p align="center"><img alt="encoding text" src="https://user-images.githubusercontent.com/59290767/129385021-895e8aa8-4ac1-4cde-a6dc-3e8a0eaffad3.png"></p><br>
<p align="center"><img alt="qr_code" src="https://user-images.githubusercontent.com/59290767/128584111-9114e0e0-98bc-441a-833c-9391323a4c08.png" width="25%"></p><br>

To encode text into QR code, use `-e` or `--encode` as given below and enter your message between " " (double quotes). You can save the QR code in any image format like `PNG`, `JPG` and even `GIF` which you can print later. Here `PNG` is used. 

```shell
python3 qr-backup.py -e "witch collapse practice feed shame open despair creek road again ice least" qr_code.png public_key.pem
```
### Encoding Text from a File
<p align="center"><img alt="endoding_file" src="https://user-images.githubusercontent.com/59290767/129385090-92db3b91-b8ce-4cfc-81be-1cf9917c19dc.png"></p><br>
<p align="center"><img alt="qr_code" src="https://user-images.githubusercontent.com/59290767/128584111-9114e0e0-98bc-441a-833c-9391323a4c08.png" width="25%"></p><br>

To encode text from a file into QR code, use `-ef` or `--encode-file` as given below. You can encrypt any file text format like `TXT`, `ASC` etc. Here `ASC` is used.

```shell
python3 qr-backup.py -ef seed.asc qr_code.png public_key.pem
```
### Scanning QR COde
<p align="center"><img alt="scannig" src="https://user-images.githubusercontent.com/59290767/130615449-25c0d274-6752-4e1f-8127-9e8f3ac74843.png"></p>
<br>

To scan the printed QR code, use `-s` or `--scan` as given below. When it shows `Scanning.....` point your webcam towards the QR code.

```shell
python3 qr-backup.py -s private_key.pem
```

### Decoding QR Code from Image
<p align="center"><img alt="decoding" src="https://user-images.githubusercontent.com/59290767/129385193-2203741a-40bf-4123-b16d-b0af185f6206.png"></p><br>

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
| `-s` | `--scan` | Scan the QR code from printed format |
| `-d` | `--decode` | Decode QR code into text |


## Donate
If you like this project then please consider to donate something.

| Bitcoin (BTC) | Ethereum (ETH) |
| --------- | ------------------- |
| <p align="center">bc1q32asnt6waz3czj4s8l7hvgnywpgatlvvvwwxyp</p> | <p align="center">0x311414BC8880BaEe435A59bdF7fdC632c3f6B8b1</p> |
| <p align="center"><img alt="btc" src="https://user-images.githubusercontent.com/59290767/128230575-0041db1a-c85a-438b-9374-ca5c96dda99c.jpg" width="35%"></p> | <p align="center"><img alt="eth" src="https://user-images.githubusercontent.com/59290767/128230627-0f5613b9-0f72-4d3d-9cd2-93a1ac5516e9.jpg" width="35%"></p> |
