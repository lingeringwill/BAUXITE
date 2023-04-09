import tkinter as tk
from recyclableDetection import bigMeatyClaws
from recyclingPickup import smallMeatyClaws

points = 0

def menu(additionalPoints=0):
    global points

    points += additionalPoints
    
    def detectRecycle():
        root.destroy()
        menu(bigMeatyClaws())

    def playGame():
        try :
            root.destroy()
            smallMeatyClaws()
        except:
            menu()
        
    # create the main window
    root = tk.Tk()
    root.title("Buaxite")
    root.geometry("1116x612")

    # create the title label
    bg = tk.PhotoImage(file="backGroundImage.png")
    canvas = tk.Canvas(root, width=1116, height = 612)
    canvas.pack()

    canvas.create_image(0,0, anchor="nw", image=bg)
    
    # create the play button
    button = tk.Button(root, width=9, height=1, text="Play", font=("Arial", 16), bg='#f6bded', command=playGame)
    canvas.create_window(603, 503, anchor="nw", window=button)

    # create the scan button
    scan_button = tk.Button(root, width=9, height=1, text="Scan", font=("Arial", 16), bg='#f6bded', command=detectRecycle)
    canvas.create_window(378, 503, anchor="nw", window=scan_button)

    # create the scan button
    point_label = tk.Label(root, width=9, height=1, text="Points: " + str(points), font=("Arial", 16), bg='#f6bded')
    canvas.create_window(500, 87, anchor="nw", window=point_label)

    # start the main loop
    root.mainloop()

menu()
