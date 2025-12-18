import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def SendLocalSMPT(sender,password, recipient, subject, body,host,port):
    try:
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain", "utf-8"))


        with smtplib.SMTP_SSL(host, port) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())

        return 0
        
    except Exception as e:
        return e