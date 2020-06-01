from nltk.corpus import wordnet 
from tkinter import *  #Tk, Label, RAISED,Button,Frame
import pyperclip
import time

# Keeps updating the copied text 
def updateClipboard():
    global cliptext
    cliptext = pyperclip.paste()
    label["text"]= cliptext 
    root.after(ms=1000, func=updateClipboard)

# Callback function of the Search button 
# Uses NLTK module
def searchMeaning():
    global labelMeaning 
    syns = wordnet.synsets(cliptext)
    labelMeaning = Label(root, text="",wraplength=400,justify="center")
    labelMeaning["text"]= syns[0].definition()
    labelMeaning.pack()

# Callback function of the Clear button 
def clearText():
    labelMeaning.destroy()
   

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x200")
    root.title("The Meaning Box")
    label = Label(root, text="", cursor="plus", relief=RAISED, pady=5,  wraplength=500)
    label.pack()
    buttonFrame= Frame(root)
    buttonFrame.pack(side= BOTTOM)
    clearButton = Button(buttonFrame, text= "Clear Text",command = clearText)
    clearButton.pack(side = LEFT)
    searchButtton = Button(buttonFrame,text = "Search",command = searchMeaning)
    searchButtton.pack(side = LEFT, fill = BOTH)
    updateClipboard()
    root.mainloop()
