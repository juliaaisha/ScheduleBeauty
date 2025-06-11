import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from appointments import AppointmentsWindow
from procedures import ProceduresWindow
from products import ProductsWindow
from reports import ReportsWindow

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Schedule Beauty")
        self.root.geometry("600x400")
        self.root.configure(bg='#ffa9f9')  # Fundo rosa
        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure('TFrame', background='#ffa9f9')
        style.configure('TLabel', background='#ffa9f9', foreground='white', font=('Helvetica', 12)) 
        style.configure('TButton', background="#ffffff", foreground='#ff8af0', font=('Arial', 12, 'bold'))

        # CRIA O FRAME PRIMEIRO
        self.frame = ttk.Frame(self.root, padding="20", style='TFrame')
        self.frame.pack(expand=True, fill=tk.BOTH)

        # === AGORA SIM, Adiciona a LOGO ===
        try:
            image = Image.open("logo.png")  # Verifique se o arquivo está no mesmo diretório
            image = image.resize((300, 300))
            self.logo_image = ImageTk.PhotoImage(image)
            logo_label = tk.Label(self.frame, image=self.logo_image, bg='#ffa9f9')
            logo_label.pack(pady=(0, 10))
            print("Logo carregada com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")
            # Placeholder se a imagem não carregar
            tk.Label(self.frame, text="LOGO", font=('Helvetica', 24), bg='#ffa9f9', fg='white').pack(pady=20)

        ttk.Label(self.frame, text="Bem-vindo ao Schedule Beauty", font=('Helvetica', 16)).pack(pady=20)

        ttk.Button(self.frame, text="Agendamentos", command=self.open_appointments).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame, text="Procedimentos", command=self.open_procedures).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame, text="Estoque de Produtos", command=self.open_products).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame, text="Relatórios", command=self.open_reports).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame, text="Sair", command=self.root.quit).pack(fill=tk.X, pady=5)

    def open_appointments(self):
        new_window = tk.Toplevel(self.root)
        new_window.transient(self.root)  # Torna a janela filha
        new_window.grab_set()  # Modal
        AppointmentsWindow(new_window)

    def open_procedures(self):
        new_window = tk.Toplevel(self.root)
        ProceduresWindow(new_window)

    def open_products(self):
        new_window = tk.Toplevel(self.root)
        ProductsWindow(new_window)

    def open_reports(self):
        new_window = tk.Toplevel(self.root)
        ReportsWindow(new_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    print("Programa iniciado")  # Verifique no terminal se esta mensagem aparece
    root.mainloop()