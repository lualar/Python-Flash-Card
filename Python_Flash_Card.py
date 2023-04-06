from tkinter import *
from FrenchWords import cRandomWord
import random

BACKGROUND_COLOR = "#B1DDC6"

#Load french words CSV File and return a Dictionary
cWord = cRandomWord()
fDict = cWord.dGetDict()
iWords = len(fDict)

#Next Card Function
def NextCard():
    #get a random card from Dict
    Current_Card = random.choice(fDict)
    
    #get French and English words from random card
    sEnglish = Current_Card["English"]
    print(f"Words: French: {Current_Card['French']} - English: {sEnglish}")

    #assing french word to French field in window
    myCanvas.itemconfig(cardFrenchTitle, text="French")
    myCanvas.itemconfig(cardFrenchWord, text=Current_Card ["French"])

#configure window
wMyWindow = Tk()
wMyWindow.title("Flash Cards")
wMyWindow.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Create a canvas to manage images
myCanvas = Canvas(width=800, height=526, highlightthickness =0,bg=BACKGROUND_COLOR)

#Create Card Image and show a french word
imFrontMyImage = PhotoImage(file="./images/card_front.png")
myCanvas.create_image(400, 263, image=imFrontMyImage)
myCanvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
myCanvas.grid(row=0, column=0, columnspan=2)

cardFrenchTitle = myCanvas.create_text(400, 150, text="Title", font=('Ariel',40, 'italic'))
cardFrenchWord = myCanvas.create_text(400, 263, text="word", font=('Ariel',60, 'bold'))

#Create Bottoms on window and link to "Next_Card" function
cross_image = PhotoImage(file="./images/wrong.png")
check_image = PhotoImage(file="./images/right.png")

myUnknowButton = Button(image=cross_image, highlightthickness=0, command=NextCard)
myUnknowButton.grid(row=1, column=0)

myCheckButton = Button(image=check_image, highlightthickness=0, command=NextCard)
myCheckButton.grid(row=1, column=1)

#Get 1st random Card
NextCard()

#running window
wMyWindow.mainloop()