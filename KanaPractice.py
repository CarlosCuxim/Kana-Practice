import random as rd
import json
import tkinter as tk
from tkinter.constants import ANCHOR
import tkinter.ttk as ttk


with open("Kana/hiragana.json", encoding="utf-8") as hiraganaJSON:
    hiragana = json.load(hiraganaJSON)

def GetRandomKana(kana):
    n = len(kana)
    k = rd.randrange(n)
    key = list(kana)[k]
    return (key, kana[key])


# Ventanas
Window = tk.Tk()
Window.minsize(500, 280)

MainFrame = tk.Frame(Window)
MainFrame.pack()

# Romaji Label
RomajiLabel = tk.Label(MainFrame, text="R", font=("Segoe UI", 100), width=3, background="white")
RomajiLabel.grid(row=0, column=0, padx=10, pady=25)

# Kana Label
KanaLabel = tk.Label(MainFrame, text="K", font=("Segoe UI", 100), width=3, background="white")
KanaLabel.grid(row=0, column=1,  padx=10, pady=25)

# Botón Frame
ButtonFrame = tk.Frame(MainFrame)
ButtonFrame.grid(row=1, column=0, columnspan=2)


# Eventos de botón =============================================================

EventBool = True

def StopEvent():
    global EventBool
    EventBool = False
    RomajiLabel.config(text="R")
    KanaLabel.config(text="K")
    LoopButton.config(text="Wait...")

def StarEvent():
    global EventBool
    EventBool = True

def StartButtonEvent():
    if EventBool:
        LoopButton.config(text="STOP", command=StopEvent)
        

        R, K = GetRandomKana(hiragana)
        RomajiLabel.config(text=R)

        KanaLabel.config(text="")
        KanaLabel.after(1000, lambda: KanaLabel.config(text="1") if EventBool else None)
        KanaLabel.after(2000, lambda: KanaLabel.config(text="2") if EventBool else None)
        KanaLabel.after(3000, lambda: KanaLabel.config(text="3") if EventBool else None)
        KanaLabel.after(4000, lambda: KanaLabel.config(text=K)   if EventBool else None)

        Window.after(5000, StartButtonEvent)
    
    else:
        StarEvent()
        LoopButton.config(text="START", command=StartButtonEvent)

ReservedKana = ""
ShowMode = True

def RandomButtonEvent():
    global  ReservedKana, ShowMode
    if ShowMode:
        R, ReservedKana = GetRandomKana(hiragana)
        RomajiLabel.config(text=R)
        KanaLabel.config(text="")

        RandomButton.config(text="SHOW")
        ShowMode = False

    else:
        KanaLabel.config(text=ReservedKana)
        RandomButton.config(text="RANDOM")
        ShowMode = True


def BindButtonEvent(event):
    RandomButtonEvent()

RandomButton = ttk.Button(ButtonFrame, text="RANDOM", command=RandomButtonEvent)
RandomButton.grid(row=0, column=0, padx=10)

LoopButton = ttk.Button(ButtonFrame, text="START", command=StartButtonEvent)
LoopButton.grid(row=0, column=1, padx=10)

Window.bind("r", BindButtonEvent)


Window.mainloop()