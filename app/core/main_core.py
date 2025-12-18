from .GlobalSMPT import SendGlobalSMPT #sender,password, recipient, subject, body
from .LocalSMPT import SendLocalSMPT #sender,password, recipient, subject, body, host,port
import csv
from base64 import b64decode, b64encode

#print(SendLocalSMPT("goida@mail.ru", "", "root@kali.localdomain", "GOIDA", "goida femboy is good", "192.168.213.128", 25))
def attack(sender,password,table,chekSMPT,host,port):
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
        try:
            #Нейросеть <- фио, должность ссылку
            if(chekSMPT == False):
                print(SendGlobalSMPT(sender,password,email[i],name[i],rab[i]))
        except Exception as e:
            print(e,email[i])
