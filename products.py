import tkinter as tk
from tkinter import ttk

class ProductsWindow:  # ← O nome exato que main.py espera
    def __init__(self, root):
        self.root = root
        self.root.title("Estoque de Produtos")
        self.root.geometry("800x600")
        self.root.configure(bg='#ffa9f9')
        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure('Treeview.Heading', background='#ff8af0', foreground='white')
        style.configure('Treeview', background='white', fieldbackground='white')

        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)

        self.tree = ttk.Treeview(frame, columns=("Produto", "Quantidade"), show="headings")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Dados de exemplo
        self.tree.insert("", tk.END, values=("Creme Facial", 15))
        self.tree.insert("", tk.END, values=("Óleo de Massagem", 8))