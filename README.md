# File-Transfer-App-Through-QR-Code


A simple Python-based file transfer app that allows users to share files via a QR code. The app creates a local HTTP server, generates a QR code with the URL of the file, and allows users to scan the QR code on their mobile devices to download the file. 

This project is ideal for sharing files in a local network without the need for an internet connection.

## Features
- Serve any file or folder from your local system over a local network.
- Generate a QR code for easy file access via mobile devices.
- Simple and easy-to-use interface with automatic file serving.
- No need for internet access, works on the same network.

## Requirements
Before you can run the project, you need to have the following installed:

- Python 3.x
- `pyqrcode` library
- `png` library (used for QR code generation)

You can install the required libraries using `pip`:
```bash
pip install pyqrcode pypng
