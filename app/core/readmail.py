import imaplib
import email
from email.utils import parseaddr
import csv
from base64 import b64encode
from .status import setStatus

def readMail(domain, table, remail, password, host, port):
    sender = []
    with open(table, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f) 
        for row in reader:
            sender.append(row.get('Email', '').strip())
    if not host or not port:
        imapDomain = remail.split("@")[-1].lower()
        if imapDomain in ("ya.ru", "yandex.ru", "yandex.com"):
            host = "imap.yandex.ru"
            port = 993
        elif imapDomain == "mail.ru":
            host = "imap.mail.ru"
            port = 993
        elif imapDomain == "gmail.com":
            host = "imap.gmail.com"
            port = 993
    m = imaplib.IMAP4_SSL(host,port)
    m.login(remail, password)
    m.select("INBOX")
    _, data = m.search(None, "UNSEEN")
    for num in data[0].split():
        _, msgData = m.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msgData[0][1])
        _, emailr = parseaddr(msg.get("From", ""))
        if emailr in sender:
            if domain in msg.as_string():
                setStatus(b64encode(emailr.encode('utf-8')).decode('ascii'),3,table)
                m.store(num, "+FLAGS", "\\Seen")
    m.logout()