import csv
from base64 import b64decode

def setStatus(id,stat, table):
    email = b64decode(id.encode('utf-8'))
    print(email, stat)

