from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#configure window
wMyWindow = Tk()
wMyWindow.title("Flash Cards")
wMyWindow.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Create a canvas to manage images
myCanvas = Canvas(width=800, height=526, highlightthickness =0,bg=BACKGROUND_COLOR)

#Create Images 
imFrontMyImage = PhotoImage(file="./images/card_front.png")
myCanvas.create_image(400, 263, image=imFrontMyImage)
myCanvas.create_text(400, 150, text="Title", font=('Ariel',40, 'italic'))
myCanvas.create_text(400, 263, text="word", font=('Ariel',60, 'bold'))
myCanvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
myCanvas.grid(row=0, column=0, columnspan=2)

#Create Bottoms
cross_image = PhotoImage(file="./images/wrong.png")
myUnknowButton = Button(image=cross_image, highlightthickness=0)
myUnknowButton.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
myCheckButton = Button(image=check_image, highlightthickness=0)
myCheckButton.grid(row=1, column=1)

#running window
wMyWindow.mainloop()