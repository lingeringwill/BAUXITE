
def menu():
    import tkinter as tk

    # create the main window
    root = tk.Tk()
    root.title("Buaxite")
    root.geometry("1000x1000")

    # create the title label
    title_label = tk.Label(root, text="Buaxite", font=("Arial", 24))
    title_label.pack(pady=20)

    # create the point balance label
    point_balance_label = tk.Label(root, text="Points: 0", font=("Arial", 12))
    point_balance_label.pack(padx=20, pady=10)

    # create the play button
    play_button = tk.Button(root, text="Play", font=("Arial", 16), width=10)
    play_button.pack(pady=10)

    # create the scan button
    scan_button = tk.Button(root, text="Scan", font=("Arial", 16), width=10)
    scan_button.pack(pady=10)

    # start the main loop
    root.mainloop()
