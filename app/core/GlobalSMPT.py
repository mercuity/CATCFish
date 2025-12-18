import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def GlobalSMPTconfig(email):
    domain = email.split("@")[-1].lower()
    
    if domain in ("ya.ru", "yandex.ru", "yandex.com"):
        return {
            "server": "smtp.yandex.ru",
            "port_ssl": 465,
            "port_tls": 587,
            "require_login": True
        }
    elif domain == "mail.ru":
        return {
            "server": "smtp.mail.ru",
            "port_ssl": 465,
            "port_tls": 587,
            "require_login": True
        }
    elif domain == "gmail.com":
        return {
            "server": "smtp.gmail.com",
            "port_ssl": 465,
            "port_tls": 587,
            "require_login": True
        }
    else:
        raise ValueError(f"'{domain}' не поддерживается. Добавьте его вручную.")

def SendGlobalSMPT(sender,password, recipient, subject, body):
    try:
        config = GlobalSMPTconfig(sender)

        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html", "utf-8"))


        with smtplib.SMTP_SSL(config["server"], config["port_ssl"]) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())

        return 0
        
    except Exception as e:
        return e
