from .GlobalSMPT import SendGlobalSMPT #sender,password, recipient, subject, body
from .LocalSMPT import SendLocalSMPT #sender,password, recipient, subject, body, host,port
import csv
from base64 import b64encode


def attack(sender,password,table,chekSMPT,host,port,domain):
    name, email, rab = [], [], []
    with open(table, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        
        for row in reader:
            name.append(row[0] if len(row) > 0 else '')
            email.append(row[1] if len(row) > 1 else '')
            rab.append(row[2] if len(row) > 2 else '')
        if len(name) != len(email) != len(rab):
            print("Таблица не полная")
            return 1 
        
    for i in range(0,len(email)):
        link = "http://"+domain+f"/login?id={b64encode(email[i].encode('utf-8')).decode('ascii')}"
        try:
            #Нейросеть <- фио, должность ссылку
            if(chekSMPT == False):
                print(SendGlobalSMPT(sender,password,email[i],name[i],link))
        except Exception as e:
            print(e,email[i])
