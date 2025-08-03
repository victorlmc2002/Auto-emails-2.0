import tkinter as tk
from tkinter import ttk, messagebox
from email_utils.envio import enviar_email_inquilino, enviar_email_proprietario

class EmailInterface:
    def __init__(self, devedores):
        self.devedores = devedores
        self.selected_items = set()
        self.root = tk.Tk()
        self.root.title("Envio de Emails - Sistema de Boletos")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Selecione os imóveis para envio de emails",
                  font=('Helvetica', 14, 'bold')).pack(pady=10)

        selection_frame = ttk.Frame(main_frame)
        selection_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.tree = ttk.Treeview(selection_frame, columns=('Nome', 'Valor'), show='headings')
        self.tree.heading('Nome', text='Proprietário/Inquilino')
        self.tree.heading('Valor', text='Endereço')

        vsb = ttk.Scrollbar(selection_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        for i, devedor in enumerate(self.devedores, 1):
            self.tree.insert("", "end", values=(f"{i} - {devedor._nome_inquilino}", f"{devedor._endereco}"), tags=(str(i),))

        self.tree.tag_configure('selected', background='lightblue')

        options_frame = ttk.Frame(main_frame)
        options_frame.pack(fill=tk.X, pady=10)

        self.recipient_var = tk.StringVar(value="inquilino")
        ttk.Radiobutton(options_frame, text="Enviar para Inquilino", variable=self.recipient_var,
                        value="inquilino").pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(options_frame, text="Enviar para Proprietário", variable=self.recipient_var,
                        value="proprietario").pack(side=tk.LEFT, padx=10)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        ttk.Button(button_frame, text="Selecionar Todos", command=self.select_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Desmarcar Todos", command=self.deselect_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Enviar Selecionados", command=self.send_selected).pack(side=tk.RIGHT, padx=5)

        self.tree.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            tags = self.tree.item(item, "tags")
            if tags:
                idx = int(tags[0])
                if idx in self.selected_items:
                    self.selected_items.remove(idx)
                    self.tree.item(item, tags=(tags[0],))
                else:
                    self.selected_items.add(idx)
                    self.tree.item(item, tags=(tags[0], 'selected'))

    def select_all(self):
        self.selected_items = set(range(1, len(self.devedores)+1))
        for item in self.tree.get_children():
            tags = self.tree.item(item, "tags")
            if tags:
                self.tree.item(item, tags=(tags[0], 'selected'))

    def deselect_all(self):
        self.selected_items = set()
        for item in self.tree.get_children():
            tags = self.tree.item(item, "tags")
            if tags:
                self.tree.item(item, tags=(tags[0],))

    def send_selected(self):
        if not self.selected_items:
            messagebox.showwarning("Nenhum selecionado", "Por favor, selecione pelo menos um imóvel.")
            return

        recipient_type = self.recipient_var.get()
        confirm = messagebox.askyesno(
            "Confirmar envio",
            f"Você está prestes a enviar emails para {len(self.selected_items)} imóveis ({recipient_type}s).\nDeseja continuar?"
        )

        if not confirm:
            return

        self.root.config(cursor="watch")
        self.root.update()

        try:
            for idx in self.selected_items:
                devedor = self.devedores[idx-1]
                if recipient_type == "inquilino":
                    enviar_email_inquilino(devedor)
                else:
                    enviar_email_proprietario(devedor)

            messagebox.showinfo("Sucesso", "Emails enviados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao enviar os emails:\n{str(e)}")
        finally:
            self.root.config(cursor="")

    def run(self):
        self.root.mainloop()
