import random as rd
import json
import tkinter as tk
import tkinter.ttk as ttk


with open("Kana/hiragana.json", encoding="utf-8") as hiraganaJSON:
    hiragana = json.load(hiraganaJSON)

def GetRandomKana(kana):
    n = len(kana)
    k = rd.randrange(n)
    key = list(kana)[k]
    return (key, kana[key])



Window = tk.Tk()
Window.minsize(500,300)

MainFrame = ttk.Frame(Window, width=400, height=300)
MainFrame.pack(pady=5)



RomajiLabel = ttk.Label(MainFrame, text="R")
RomajiLabel.grid(row=0, column=0)

KanaLabel = ttk.Label(MainFrame, text="K")
KanaLabel.grid(row=0, column=1)


def RandomButtonEvent():
    R, K = GetRandomKana(hiragana)
    RomajiLabel.config(text=R)
    KanaLabel.config(text=K)


RandomButton = ttk.Button(MainFrame, text="RANDOM", command=RandomButtonEvent)
RandomButton.grid(row=1, column=0, columnspan=2)





Window.mainloop()