import tkinter as tk
from tkinter import ttk
from core.readmail import readMail 

def create_tab3(parent, controls):
    frame = ttk.Frame(parent, padding=20)

    def read():
        domain = controls["domain"].get().strip()
        table = controls["tablePath"].get().strip()
        readEmail = controls["emailRead"].get().strip()
        readPassword = controls["passwordRead"].get().strip()
        host = controls["host"].get().strip()
        port = controls["port"].get().strip()
        readMail(domain,table,readEmail,readPassword,host,port)
    start_btn = ttk.Button(frame, text="Прочитать почту", command=read)
    start_btn.grid(row=0, column=0, pady=20)

    return frame