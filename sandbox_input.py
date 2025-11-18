import tkinter as tk

def create_typing_window():
    root = tk.Tk()
    root.title("CyberSec SIG - Safe Typing Box")
    root.geometry("500x300")

    label = tk.Label(root, text="Type ONLY inside this box.\nKeystrokes here are logged safely.",
                     font=("Arial", 14))
    label.pack(pady=10)

    text_area = tk.Text(root, font=("Arial", 16), wrap="word")
    text_area.pack(expand=True, fill="both")

    # This widget is where the keylogger listens
    text_area.focus_set()

    root.mainloop()

if __name__ == "__main__":
    create_typing_window()
