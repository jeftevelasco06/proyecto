import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        root.title("Lista de Tareas")
        root.geometry("400x400")
        
        # Entrada para nueva tarea
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        # Botón para agregar tarea
        self.add_button = tk.Button(root, text="Agregar Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Lista de tareas
        self.task_listbox = tk.Listbox(root, font=("Arial", 14), selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        # Botón para eliminar tarea
        self.delete_button = tk.Button(root, text="Eliminar Selección", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Configurar grid para que se adapte al tamaño
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
    
    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "Por favor escribe una tarea.")
    
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
        else:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
