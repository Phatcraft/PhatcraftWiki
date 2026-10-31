# PHATCRAFTWIKI SERVER
# Copyright 2026 Phatcraft


# LIBRARIES
from dotenv import load_dotenv
import os


# SERVER CONFIG
load_dotenv()
CONFIGS = {
    # Server ports
    "HTTP_PORT"  : int(os.getenv("HTTP_PORT")),
    "HTTPS_PORT" : int(os.getenv("HTTPS_PORT")),

    # TLS
    "DOMAIN"     : os.getenv("DOMAIN"),
    "CERT_FILE"  : os.getenv("CERT"),
    "KEY_FILE"   : os.getenv("KEY"),

    # Storage unit
    "KILOBYTE"   : 1024,
    "BUFFER_SIZE": 6,

    # HTTP Codes
    "HTTP_CODES" : { 200: "OK", 404: "Not Found", 302: "Found" }
}

# MAIN SERVER
if __name__ == "__main__":
    for key, value in CONFIGS.items():
        print(f"{key}: {value}\n")

