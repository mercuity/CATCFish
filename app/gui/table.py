import tkinter as tk
from tkinter import ttk
import csv
import os

def create_tab2(parent, tablePath):
    frame = ttk.Frame(parent, padding=20)
    frame.pack(fill="both", expand=True)

    tree_frame = ttk.Frame(frame)
    tree_frame.pack(fill="both", expand=True)

    tree = ttk.Treeview(tree_frame, show="headings")  
    vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    def update_table():

        for item in tree.get_children():
            tree.delete(item)

        tree["columns"] = ()  
        path = tablePath.get()
        if not path or not os.path.isfile(path):
            tree["columns"] = ("status",)
            tree.heading("status", text="Состояние")
            tree.column("status", anchor="w", width=400)
            tree.insert("", "end", values=("Таблица не выбрана или файл не найден",))
            return

        try:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                rows = list(reader)
                if not rows:
                    tree["columns"] = ("status",)
                    tree.heading("status", text="Состояние")
                    tree.column("status", anchor="w", width=300)
                    tree.insert("", "end", values=("Файл пуст",))
                    return

                headers = rows[0]
                if not headers:
                    tree["columns"] = ("status",)
                    tree.heading("status", text="Состояние")
                    tree.column("status", anchor="w", width=300)
                    tree.insert("", "end", values=("Первая строка (заголовки) пустая",))
                    return
                
                tree["columns"] = headers
                for col in headers:
                    tree.heading(col, text=col, anchor="w")
                    tree.column(col, anchor="w", minwidth=80, width=100, stretch=True)
                    
                for row in rows[1:]:
                    row = (row + [''] * len(headers))[:len(headers)]
                    tree.insert("", "end", values=row)

        except Exception as e:
            print( f"Ошибка: {type(e).__name__}: {e}")
    btn = ttk.Button(frame, text="Обновить", command=update_table)
    btn.pack(pady=5)
    update_table()
    return frame