# gui_sample.py
"""
Minimal Tkinter GUI placeholder for live engine display.
Purely illustrative.
"""

import tkinter as tk

class EngineGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Options Engine - Demo GUI")

        self.status_label = tk.Label(
            self.root, text="Engine Status: IDLE", font=("Arial", 14)
        )
        self.status_label.pack(pady=10)

        tk.Button(
            self.root,
            text="Start Engine",
            command=self.start_engine
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Stop Engine",
            command=self.stop_engine
        ).pack(pady=5)

    def start_engine(self):
        self.status_label.config(text="Engine Status: RUNNING")

    def stop_engine(self):
        self.status_label.config(text="Engine Status: STOPPED")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    EngineGUI().run()
