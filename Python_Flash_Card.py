from os import remove
from tkinter import *
from FrenchWords import cRandomWord
import random

BACKGROUND_COLOR = "#B1DDC6"
TIME_TO_FLIP = 3000

#Load french words CSV File and return a Dictionary
cWord = cRandomWord()
fDict = cWord.dGetDict()
iWords = len(fDict)
Current_Card = {}

#Next Card Function
def NextCard():
    global Current_Card, tFlipTimer
    
    #Invalide the previous timer and start again
    wMyWindow.after_cancel(tFlipTimer)
    
    #get a random card from Dict
    Current_Card = random.choice(fDict)
    
    #Print French and English words from random card
    #print(f"Words: French: {Current_Card['French']} - English: {Current_Card ['English']}")

    #assing french word to French field in window
    myCanvas.itemconfig(myCanvasImage, image=imFrontMyImage)    #Change card image to front
    myCanvas.itemconfig(cardFrenchTitle, text="French")
    myCanvas.itemconfig(cardFrenchWord, text=Current_Card ["French"], fill="black")
    #Wait for some time a flip the card
    tFlipTimer = wMyWindow.after(TIME_TO_FLIP, func=FlipCard)

#User already know the word. Remove this card from the dictionary
def NextCardOK():
    RemoveCard() #Remove the flash card from dict
    NextCard()  #Get next flash card
 
#Function flip the card and show the English translation of the word
def FlipCard():
    global Current_Card  #Storage the current flash card
    myCanvas.itemconfig(myCanvasImage, image=imBackImage)    #Change card image to back
    myCanvas.itemconfig(cardFrenchTitle, text="English")    #change title from French to English
    myCanvas.itemconfig(cardFrenchWord, text=Current_Card ['English'], fill="white")

#remove card from dict and save the new list on CSV file
def RemoveCard():
    fDict.remove(Current_Card)
    cWord.fSaveWordsToLearn(fDict)

#configure window
wMyWindow = Tk()
sTitle = "Flash Cards: " + str(iWords)  + " words to play!"
wMyWindow.title(sTitle)
wMyWindow.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Wait for some time a flip the card
tFlipTimer = wMyWindow.after(TIME_TO_FLIP, func=FlipCard)

#Create a canvas to manage images
myCanvas = Canvas(width=800, height=526, highlightthickness =0,bg=BACKGROUND_COLOR)
myCanvas.pack()

#Create Card Image and load the front card
imFrontMyImage = PhotoImage(file="./images/card_front.png")
imBackImage = PhotoImage(file="./images/card_back.png")

#Create canvas image and assing backgrund color
myCanvasImage = myCanvas.create_image(400, 263, image=imFrontMyImage)
myCanvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
myCanvas.grid(row=0, column=0, columnspan=2)

#create fields for title and word (French or English)
cardFrenchTitle = myCanvas.create_text(400, 150, text="Title", font=('Ariel',40, 'italic'))
cardFrenchWord = myCanvas.create_text(400, 263, text="word", font=('Ariel',60, 'bold'))

#Create Bottoms on window and link to "Next_Card" function
cross_image = PhotoImage(file="./images/wrong.png")
check_image = PhotoImage(file="./images/right.png")

#create buttons and assing next card function
myUnknowButton = Button(image=cross_image, highlightthickness=0, command=NextCard)
myUnknowButton.grid(row=1, column=0)

myCheckButton = Button(image=check_image, highlightthickness=0, command=NextCardOK)
myCheckButton.grid(row=1, column=1)

#Get 1st random Card
NextCard()

#running window
wMyWindow.mainloop()