import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

# Create the main window
window = tk.Tk()
window.title("Simple Tkinter Example")

# Create a button and a label
button = tk.Button(window, text="Click me!", command=on_button_click)
label = tk.Label(window, text="Welcome to Tkinter!")

# Pack the button and label into the window
button.pack(pady=10)
label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()

