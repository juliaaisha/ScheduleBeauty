import tkinter as tk
from tkinter import ttk
import subprocess
import os
import sqlite3
from tkcalendar import Calendar
from tkinter import messagebox

# Janela de Agendamentos
class AppointmentsWindow:
    def __init__(self, parent):
        self.root = tk.Toplevel(parent)
        self.root.title("Agendamentos")
        self.root.geometry("800x600")
        self.root.configure(bg='#ffa9f9')
        self.root.transient(parent)
        self.root.grab_set()
        self.setup_ui()

    def setup_ui(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)

        ttk.Label(frame, text="Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.client_entry = ttk.Entry(frame, width=40)
        self.client_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Data:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.cal = Calendar(frame, selectmode='day', date_pattern='dd/mm/yyyy')
        self.cal.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Procedimento:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.procedure_cb = ttk.Combobox(frame, values=["Limpeza de Pele", "Massagem", "Drenagem"])
        self.procedure_cb.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Salvar", command=self.save_appointment).grid(row=3, column=1, pady=10, sticky=tk.E)

    def save_appointment(self):
        cliente = self.client_entry.get()
        data = self.cal.get_date()
        procedimento = self.procedure_cb.get()

        if not cliente or not procedimento:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        conn = sqlite3.connect('agendamentos.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO agendamentos (cliente, data, procedimento)
            VALUES (?, ?, ?)
        ''', (cliente, data, procedimento))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Agendamento salvo com sucesso!")
        self.client_entry.delete(0, tk.END)
        self.procedure_cb.set("")

# Criação do banco
def criar_tabela():
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            data TEXT NOT NULL,
            procedimento TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


