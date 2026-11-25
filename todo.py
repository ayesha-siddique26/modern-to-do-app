import tkinter as tk
from tkinter import messagebox
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ayesha's To-Do List")
        self.root.geometry("500x600")
        self.root.config(bg="#f0f0f0")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        # Title
        title = tk.Label(root, text="✨ My To-Do List ✨", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#6C3483")
        title.pack(pady=15)

        # Entry Frame
        frame = tk.Frame(root, bg="#f0f0f0")
        frame.pack(pady=5)

        self.entry = tk.Entry(frame, font=("Arial", 13), width=30, bd=2, relief="solid")
        self.entry.pack(side="left", padx=5)
        self.entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(frame, text="Add +", font=("Arial", 12, "bold"), bg="#6C3483", fg="white", width=8, command=self.add_task, cursor="hand2")
        add_btn.pack(side="left", padx=5)

        # Listbox
        self.listbox = tk.Listbox(root, font=("Arial", 13), width=42, height=15, bd=2, selectbackground="#D2B4DE")
        self.listbox.pack(pady=15)
        self.refresh_list()

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack(pady=5)

        done_btn = tk.Button(btn_frame, text="✅ Done", font=("Arial", 11, "bold"), bg="#27AE60", fg="white", width=10, command=self.mark_done)
        done_btn.grid(row=0, column=0, padx=5)

        del_btn = tk.Button(btn_frame, text="🗑 Delete", font=("Arial", 11, "bold"), bg="#E74C3C", fg="white", width=10, command=self.delete_task)
        del_btn.grid(row=0, column=1, padx=5)

        clear_btn = tk.Button(btn_frame, text="Clear All", font=("Arial", 11, "bold"), bg="#F39C12", fg="white", width=10, command=self.clear_all)
        clear_btn.grid(row=0, column=2, padx=5)

        # Footer
        footer = tk.Label(root, text="Made by Ayesha Siddique ❤️", font=("Arial", 10), bg="#f0f0f0", fg="gray")
        footer.pack(side="bottom", pady=10)

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for t in self.tasks:
            prefix = "✅ " if t["done"] else "📌 "
            self.listbox.insert(tk.END, prefix + t["text"])

    def add_task(self):
        text = self.entry.get().strip()
        if text == "":
            messagebox.showwarning("Warning", "Pehle koi kaam likho!")
            return
        self.tasks.append({"text": text, "done": False})
        self.entry.delete(0, tk.END)
        self.save_tasks()
        self.refresh_list()

    def mark_done(self):
        try:
            i = self.listbox.curselection()[0]
            self.tasks[i]["done"] = not self.tasks[i]["done"]
            self.save_tasks()
            self.refresh_list()
        except:
            messagebox.showwarning("Warning", "Pehle koi kaam select karo!")

    def delete_task(self):
        try:
            i = self.listbox.curselection()[0]
            del self.tasks[i]
            self.save_tasks()
            self.refresh_list()
        except:
            messagebox.showwarning("Warning", "Pehle koi kaam select karo!")

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Saara kaam delete kar dun?"):
            self.tasks = []
            self.save_tasks()
            self.refresh_list()

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                try:
                    self.tasks = json.load(f)
                except:
                    self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
    