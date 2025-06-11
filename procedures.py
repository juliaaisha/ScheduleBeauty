import tkinter as tk
from tkinter import ttk

class ProceduresWindow:  # <-- Nome exato que o main.py espera
    def __init__(self, root):
        self.root = root
        self.root.title("Procedimentos")
        self.root.geometry("600x400")
        self.root.configure(bg='#ffa9f9')
        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure('TFrame', background='#ffa9f9')
        style.configure('TLabel', background='#ffa9f9', foreground='white')
        style.configure('TButton', background='#ff8af0', foreground='white')

        frame = ttk.Frame(self.root, padding="20", style='TFrame')
        frame.pack(expand=True, fill=tk.BOTH)

        ttk.Label(frame, text="Nome do Procedimento:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(frame, width=40).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Produtos Utilizados:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)
        tk.Listbox(frame, selectmode=tk.MULTIPLE, width=40, height=10).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Salvar Procedimento").grid(row=2, column=1, pady=10, sticky=tk.E)