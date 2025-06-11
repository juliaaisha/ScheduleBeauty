import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class ReportsWindow:  # ← NOME EXATO que main.py espera
    def __init__(self, root):
        self.root = root
        self.root.title("Relatórios")
        self.root.geometry("700x500")
        self.root.configure(bg='#ffa9f9')
        self.setup_ui()

    def setup_ui(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)

        ttk.Label(frame, text="Selecione o período:").pack()
        self.cal_start = Calendar(frame, date_pattern='dd/mm/yyyy')
        self.cal_start.pack(pady=10)

        ttk.Button(frame, text="Gerar Relatório").pack(pady=20)

