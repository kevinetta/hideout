import random
import Tkinter
import os

def GetArray(difficulty):
    filepath = os.path.dirname(__file__)
    path = os.path.join(filepath, "../../res/" + difficulty + ".txt")
    
    with open(path) as inputfile:
        array = inputfile.readlines()
    return array

top = Tkinter.Tk("Hideout")
top.title("Hideout")
#fix size issue
resultTxt = Tkinter.Text(top)

def Generate(difficulty):
    resultTxt.delete(Tkinter.CURRENT, Tkinter.END)
    if (difficulty == "easy") | (difficulty == "medium") | (difficulty == "hard"):
        difArray = GetArray(difficulty)
        result = difArray[random.randint(0,len(difArray)-1)]
        resultTxt.insert(Tkinter.END,chars=str(result))
    else:
        resultTxt.insert(Tkinter.END,chars=("Invalid Input"))

easyBtn = Tkinter.Button(
    master=top,
    text="easy",
    bg="green",
    command=lambda: Generate("easy")
).pack()
mediumBtn = Tkinter.Button(
    master=top,
    text="medium",
    bg="yellow",
    command=lambda: Generate("medium")
).pack()
hardBtn = Tkinter.Button(
    master=top,
    text="hard",
    bg="red",
    command=lambda: Generate("hard")
).pack()

resultTxt.pack()
top.mainloop()