import tkinter as tk
from tkinter import ttk

from .start import create_tab1
from .table import create_tab2
from .reuslt import create_tab3
#from AI_gui import create_tab4

def start_gui():
    root = tk.Tk()
    root.title("CATCFish (by mercuit)")
    root.geometry("800x600")

    tablePath = tk.StringVar(value="Таблица не выбрана")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both", padx=10, pady=10)

    controls, tab1 = create_tab1(notebook, tablePath)
    tab2 = create_tab2(notebook, tablePath)
    tab3 = create_tab3(notebook, controls)
    #tab4 = create_tab4(notebook)

    notebook.add(tab1, text="Старт")
    notebook.add(tab2, text="Таблица")
    notebook.add(tab3, text="Результаты")
    #notebook.add(tab4, text="Нейросеть")

    root.mainloop()