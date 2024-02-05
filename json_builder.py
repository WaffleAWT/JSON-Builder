import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from ttkthemes import ThemedTk

class JsonBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Builder - WaffleAWT")
        self.root.geometry("563x288")

        self.json_data = {}
        self.last_key = ""

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.style = ttk.Style(self.root)
        self.style.theme_use("equilux")

        self.key_label = ttk.Label(self.main_frame, text="Key:")
        self.key_label.grid(row=0, column=0, sticky=tk.W)

        self.key_entry = ttk.Entry(self.main_frame)
        self.key_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))

        self.create_key_button = ttk.Button(self.main_frame, text="Create Key", command=self.create_key)
        self.create_key_button.grid(row=0, column=3, sticky=tk.W)

        self.property_label = ttk.Label(self.main_frame, text="Property:")
        self.property_label.grid(row=1, column=0, sticky=tk.W)

        self.property_entry = ttk.Entry(self.main_frame)
        self.property_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        self.value_label = ttk.Label(self.main_frame, text="Value:")
        self.value_label.grid(row=1, column=2, sticky=tk.W)

        self.value_entry = ttk.Entry(self.main_frame)
        self.value_entry.grid(row=1, column=3, sticky=(tk.W, tk.E))

        self.create_property_button = ttk.Button(self.main_frame, text="Create Property", command=self.create_property)
        self.create_property_button.grid(row=1, column=4, sticky=tk.W)

        self.json_display_label = ttk.Label(self.main_frame, text="Generated JSON:")
        self.json_display_label.grid(row=2, column=0, sticky=tk.W)

        self.json_display = tk.Text(self.main_frame, height=10, width=50, state=tk.DISABLED)
        self.json_display.grid(row=3, column=0, columnspan=5, sticky=(tk.W, tk.E))

        self.clear_button = ttk.Button(self.main_frame, text="Clear", command=self.clear_json)
        self.clear_button.grid(row=4, column=0, sticky=tk.W)

        self.save_button = ttk.Button(self.main_frame, text="Save JSON", command=self.save_json)
        self.save_button.grid(row=4, column=1, sticky=tk.W)

        self.load_button = ttk.Button(self.main_frame, text="Load JSON", command=self.load_json)
        self.load_button.grid(row=4, column=2, sticky=tk.W)

    def create_key(self):
        key = self.key_entry.get()
        if key:
            self.json_data[key] = {}
            self.last_key = key
            self.update_json_display()
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, self.last_key)

    def create_property(self):
        key = self.key_entry.get()
        property_name = self.property_entry.get()
        property_value = self.value_entry.get()

        if key and property_name:
            if property_value.startswith("[") and property_value.endswith("]"):
                try:
                    property_value = json.loads(property_value)
                except json.JSONDecodeError:
                    pass

            self.json_data[key][property_name] = property_value
            self.property_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)
            self.update_json_display()

    def update_json_display(self):
        json_str = json.dumps(self.json_data, indent=2)
        self.json_display.config(state=tk.NORMAL)
        self.json_display.delete(1.0, tk.END)
        self.json_display.insert(tk.END, json_str)
        self.json_display.config(state=tk.DISABLED)

    def clear_json(self):
        self.json_data = {}
        self.last_key = ""
        self.key_entry.delete(0, tk.END)
        self.property_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.update_json_display()

    def save_json(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(self.json_data, file, indent=2)

            messagebox.showinfo("Save JSON", "JSON saved successfully.")

    def load_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.json_data = json.load(file)
                self.update_json_display()
            except json.JSONDecodeError as e:
                messagebox.showerror("Error", f"Error loading JSON file: {e}")

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = JsonBuilder(root)
    root.mainloop()

# Follow me on @github: github.com/waffleawt :)
    