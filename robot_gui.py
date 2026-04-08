import tkinter as tk
from tkinter import simpledialog
def main():
    root = tk.Tk()
    root.title('Robot Control Panel')

    def handle_command():
        response = simpledialog.askstring('Input', 'Enter a command for the robot:')
        print(f'Command received: {response}')
        
    command_button = tk.Button(root, text='Send Command', command=handle_command)
    command_button.pack(pady=20)

    exit_button = tk.Button(root, text='Exit', command=root.destroy)
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
