import tkinter as tk
from tkinter import ttk, filedialog
import csv
import os
from datetime import datetime
from core.main_core import attack
from core.site import create_app
import threading

def create_tab1(parent, tablePath):
    frame = ttk.Frame(parent, padding=20)

    localSMPT = tk.BooleanVar(value=False)

    def select_file():
        path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("CSV файлы", "*.csv"), ("Все файлы", "*.*")]
        )
        if not path:
            print("Путь пустой")
            return
        with open(path, newline='', encoding='utf-8') as table:
                reader = csv.DictReader(table)
                rows = list(reader)
                fieldnames = reader.fieldnames or []
        if not fieldnames:
                raise ValueError("Файл пуст или без заголовков")
        tablename = fieldnames + ["Статус"]
        tableRows = []
        for row in rows:
            tableRows.append({**row, "Статус": "Атака не начата"})
        base, ext = os.path.splitext(path)
        tablePath.set(f"{base}_{datetime.now().strftime("%Y%m%d_%H%M%S")}{ext}")
        with open(tablePath.get(), 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=tablename)
            writer.writeheader()
            writer.writerows(tableRows)
        fileLabel.config(text=os.path.basename(tablePath.get()), foreground="black")

    #Почта
    ttk.Label(frame, text="Отправитель:").grid(row=0, column=0, sticky="w", pady=(0, 5))
    sender = ttk.Entry(frame, width=40)
    sender.grid(column=0, pady=(0, 15))

    #Пароль
    ttk.Label(frame, text="Пароль:").grid(row=2, column=0, sticky="w", pady=(0, 5))
    password = ttk.Entry(frame, show="*", width=40)
    password.grid(column=0, pady=(0, 15))

    #Выбор таблицы
    table = ttk.Button(frame, text="Выбрать таблицу", command=select_file)
    table.grid(row=6, column=0, pady=(0, 15))

    fileLabel = ttk.Label(frame, text="Таблица не выбрана", foreground="gray")
    fileLabel.grid(row=6, column=1, pady=(0, 15))

    #Local SMPT
    chekSMPT = ttk.Checkbutton(frame, text="Local SMPT Server", variable=localSMPT, onvalue=True, offvalue=False)
    chekSMPT.grid(row=0, column=1, sticky="w", pady=(0, 15))
    
    #Хост
    ttk.Label(frame, text="Хост:").grid(row=0, column=2, sticky="w", pady=(0, 5))
    host = ttk.Entry(frame, width=40)
    host.grid(row=1,column=2, pady=(0, 15))

    #Порт
    ttk.Label(frame, text="Порт:").grid(row=3, column=2, sticky="w", pady=(0, 5))
    port = ttk.Entry(frame, width=40)
    port.grid(row=3,column=2, pady=(0, 15))
    
    #domain
    ttk.Label(frame, text="Домен:").grid(row=4, column=0, sticky="w", pady=(0, 5))
    domain = ttk.Entry(frame, width=40)
    domain.grid(row=5,column=0, pady=(0, 15))
    
    def attacks():
        app = create_app(tablePath.get())
        def runServer():
            app.run(host='0.0.0.0', port=80, threaded=True)
        server_thread = threading.Thread(target=runServer, daemon=True)
        server_thread.start()
        attack(sender.get(),password.get(),tablePath.get(),localSMPT.get(),host.get(),port.get(), domain.get())
        
    
    #Кнопка запуска
    start_btn = ttk.Button(frame, text="Запустить тестирование", command=attacks) 
    start_btn.grid(column=1)

    host.config(state="disabled")
    port.config(state="disabled")
            
    def select_localSMPT(*_):
        if localSMPT.get():
            host.config(state="normal")
            port.config(state="normal")
        else:
            host.config(state="disabled")
            port.config(state="disabled")
    localSMPT.trace_add("write", select_localSMPT)
    
    return frame
