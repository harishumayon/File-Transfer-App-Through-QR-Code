# Import necessary modules
import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os

# Assigning the appropriate port value
PORT = 8010

# Path to the specific file you want to share
file_path = r"C:\Users\MBAns\Desktop\File Transfer App\Capture.PNG"  #Replace this with your file path

# Validate if the file exists
if not os.path.isfile(file_path):
    print("Error: The specified file does not exist.")
    exit()

# Extract the directory and file name
directory_to_serve = os.path.dirname(file_path)
file_name = os.path.basename(file_path)

# Change the directory to the folder containing the file
os.chdir(directory_to_serve)

# Create a basic HTTP request handler
Handler = http.server.SimpleHTTPRequestHandler

# Find the IP address of the machine
hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP + "/" + file_name  # Add the file name to the URL

# Generate a QR code for the file URL
url = pyqrcode.create(link)
url.svg("file_qr.svg", scale=8)

# Open the QR code in the browser
webbrowser.open('file_qr.svg')

# Start the HTTP server to serve the file's directory
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("Direct file link:", link)
    print("Scan the QR Code to access the file.")
    httpd.serve_forever()
