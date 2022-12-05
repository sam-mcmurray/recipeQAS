import tkinter as tk

# Initialize application
root = tk.Tk()
# App Title
root.title("Recipe Finder")
# Center Window
x = (root.winfo_screenwidth() // 2) - 350
y = int(root.winfo_screenheight() * 0.2)
root.geometry("700x700+" + str(x) + '+' + str(y))
root.config(bg="#314363")


def load_frame1():
    frame1 = tk.Frame(root, width=1500, height=600, bg="#404d6d")

