# Python program to open the
# camera in Tkinter
# Import the libraries,
# tkinter, cv2, Image and ImageTk
  
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import sys
sys.path.append("C:\\Users\\Eppat\\recycleDetectionMain\\yolov5")
from detect import run
import shutil
from mainMenu import menu


labels_dict = {  0: "bottle-blue",
  1: "green bottle",
  2: "dark bottle",
  3: "bottle of milk",
  4: "transparent bottle",
  5: "multicolored bottle",
  6: "bottle of yogurt",
  7: "bottle of oil",
  8: "can",
  9: "juice box",
  10: "milk box",
  11: "colored detergent box",
  12: "transparent detergrent box",
  13: "detergent box",
  14: "canister",
  15: "full blue bottle",
  16: "full transparent bottle",
  17: "full dark bottle",
  18: "full green bottle",
  19: "full multicolored bottle",
  20: "full bottle of milk",
  21: "full bottle of oil",
  22: "white detergent container",
  23: "blue bottle",
  24: "full blue bottle",
  25: "transparent glass bottle",
  26: "dark glass bottle",
  27: "green glass bottle"}

points_dict = { "bottle-blue" : 5,
  "green bottle" : 5,
  "dark bottle" : 10,
  "bottle of milk" : 3,
  "transparent bottle" : 3,
  "multicolored bottle" : 10,
  "bottle of yogurt" : 10,
  "bottle of oil" : 3,
  "can" : 5,
  "juice box" : 5,
  "milk box" : 10,
  "colored detergent box" : 10,
  "transparent detergrent box" : 10,
  "detergent box" : 5,
  "canister" : 15,
  "full blue bottle" : 10,
  "full transparent bottle" : 10,
  "full dark bottle" : 10,
  "full green bottle" : 10,
  "full multicolored bottle" : 10,
  "full bottle of milk" : 10,
  "full bottle of oil" : 10,
  "white detergent container" : 5,
  "blue bottle" : 10,
  "full blue bottle" : 40,
  "transparent glass bottle" : 10,
  "dark glass bottle" : 12,
  "green glass bottle" : 30}


# Define a video capture object
vid = cv2.VideoCapture(0)
  
# Declare the width and height in variables
width, height = 800, 600
  
# Set the width and height
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
  
# Create a GUI app
app = Tk()
  
# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())
  
# Create a label and display it on app
label_widget = Label(app)
label_widget.pack()

text_label_name = Label(app, text="Congrats! You found a ", font="Helvetica, 16")
text_label_points = Label(app, text="Congrats! Point Value: ", font="Helvetica, 16")
  
# Create a function to open camera and
# display it in the label_widget on app

global photo_taken
photo_taken = False
  
def open_camera(photo=''):
    global photo_taken
    if not photo_taken:
        taken, frame = vid.read()
        if taken:
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image)
            photo_image = ImageTk.PhotoImage(image=captured_image)
            label_widget.photo_image = photo_image
            label_widget.configure(image=photo_image)
            label_widget.after(10, open_camera)
    else:
        try: 
            opencv_image = cv2.imread(photo)
            opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image)
            photo_image = ImageTk.PhotoImage(image=captured_image)
            label_widget.photo_image = photo_image
            label_widget.configure(image=photo_image)
            label_widget.configure(text="Congratulations! Point Value: 10 points")
        except:
            pass

def quitApp():
    vid.release()
    app.destroy()
    menu()

def take_photo():
    global photo_taken
    photo_taken = True
    # capture a frame from the camera
    ret, frame = vid.read()
    
    # save the frame as a JPEG file
    cv2.imwrite("photo.jpg", frame)
    
    run(source="C:\\Users\\Eppat\\recycleDetectionMain\\photo.jpg", weights="C:/Users/Eppat/recycleDetectionMain/yolov5/runs/train/exp7/weights/best.pt", conf_thres=0.05, save_txt=True, save_conf=True)


    
    image_name = os.listdir("C:\\Users\\Eppat\\recycleDetectionMain\\yolov5\\runs\\detect\\exp\\")[-1]
    print("C:\\Users\\Eppat\\recycleDetectionMain\\yolov5\\runs\\detect\\exp\\" + image_name)
    open_camera("C:\\Users\\Eppat\\recycleDetectionMain\\yolov5\\runs\\detect\\exp\\" + image_name)

    highest_conf = 0
    idItem = None
    detected_info = open("C:\\Users\\Eppat\\recycleDetectionMain\\yolov5\\runs\\detect\\exp\\labels\\photo.txt")
    for x in detected_info:
        if float(x.split(" ")[-1].strip("\n")) > highest_conf:
            highest_conf = float(x.split(" ")[-1].strip("\n"))

    detected_info.close()
    detected_info = open("C:\\Users\\Eppat\\recycleDetectionMain\\yolov5\\runs\\detect\\exp\\labels\\photo.txt")
    for x in detected_info:
        if float(x.split(" ")[-1].strip("\n")) == highest_conf:
            idItem = int(x.split(" ")[0].strip("\n"))
            break
    detected_info.close()
    shutil.rmtree("C:\\Users\\Eppat\\recycleDetectionMain\\yolov5\\runs\\detect\\exp")

    text_label_name.configure(text="Congrats! You found a " + str(labels_dict[idItem]), font="Helvetica, 16")
    text_label_points.configure(text="Congrats! Point Value: " + str(points_dict[labels_dict[idItem]]), font="Helvetica, 16")

    button2.destroy()
    button1.pack()
    text_label_name.pack()
    text_label_points.pack()
  
# Create a button to open the camera in GUI app
button1 = Button(app, text="Return to Main Menu", command=quitApp)
button1.pack()

button2 = Button(app, text="Take photo", command=take_photo)
button2.pack()



open_camera()

# Create an infinite loop for displaying app on screen
app.mainloop()
