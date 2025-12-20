import tkinter as tk
from tkinter import ttk
from core.readmail import readMail 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter
import csv

def create_tab3(parent, controls, tablePath):
    frame = ttk.Frame(parent, padding=20)
    def read():
        domain = controls["domain"].get().strip()
        table = controls["tablePath"].get().strip()
        readEmail = controls["emailRead"].get().strip()
        readPassword = controls["passwordRead"].get().strip()
        host = controls["host"].get().strip()
        port = controls["port"].get().strip()
        readMail(domain, table, readEmail, readPassword, host, port)

    def chart():
        stat = []
        with open(tablePath.get().strip(), newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                stat.append(row[3] if len(row) > 3 else '')

        counts = Counter(stat)
        labels = list(counts.keys())
        sizes = list(counts.values())

        for widget in chart_frame.winfo_children():
            widget.destroy()
            
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title("Статусы писем")
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
    start_btn = ttk.Button(frame, text="Прочитать почту", command=read)
    start_btn.grid(row=0, column=0, pady=10)
    pie_btn = ttk.Button(frame, text="Показать диаграмму", command=chart)
    pie_btn.grid(row=1, column=0, pady=10)
    chart_frame = ttk.Frame(frame)
    chart_frame.grid(row=2, column=0, pady=20)

    return frame