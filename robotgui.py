import tkinter as tk
from tkinter import ttk

class RobotGUI:
    def __init__(self, scientists_data):
        self.window = tk.Tk()
        self.window.title("Scientists Information")
        self.window.geometry("1900x1000")
        # Create a frame to hold the labels and text widgets
        frame = ttk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas widget to hold the frame
        canvas = tk.Canvas(frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Configure the canvas to expand with the frame
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a new frame inside the canvas to hold the labels and text widgets
        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        self.create_labels(inner_frame, scientists_data)

        # Configure the canvas to scroll with the scrollbar
        inner_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    
    def create_labels(self, frame, scientists_data):
        # Create labels to display the information
        label_names = ["Scientist:", "Birth Date:", "Death Date:", "Age:", "Introduction:"]
        for i, label_name in enumerate(label_names):
            label = tk.Label(frame, text=label_name)
            label.grid(row=0, column=i, sticky="e", padx=10, pady=5)

        for i, scientist_data in enumerate(scientists_data):
            for j, label_name in enumerate(label_names[:-1]):
                info = tk.Label(frame, text=scientist_data[label_name.lower()[:-1].replace(" ", "_")])
                info.grid(row=i+1, column=j, sticky="w", padx=10, pady=5)
            description_text = tk.Text(frame, width=93, height=11, wrap="word")
            description_text.insert(tk.END, scientist_data["intro_paragraph"])
            description_text.grid(row=i+1, column=len(label_names), sticky="w", padx=10, pady=5)

    
    def run(self):
        self.window.mainloop()
