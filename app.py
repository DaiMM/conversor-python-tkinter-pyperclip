
import pyperclip
import tkinter as tk

root = tk.Tk()
root.title("PX >REM")
root.attributes("-topmost", True)


def inputClear():
    inputLbl.delete(0, "end")

def inputData():
    value = inputLbl.get()
    return value

def display(copiedContent):
    base = inputBaseLbl.get()
    if base == '':
        base = 16
    try:
        float(copiedContent)
    except:
        return
    
    px = float(copiedContent)
    rem = round(px/float(base), 3)
    text = (f"{px}px = {rem}rem")
    return text

def conversor():

    copied = pyperclip.paste()
  
    if inputData() == "": 
        sendData = copied
        
    else:
        sendData = inputData()
       
    lbl.config(text = display(sendData))
    lbl.after(1000, conversor)


txtLbl = tk.Label(root, text="px --> rem", foreground="#0E051F", font=("calibri", 14, "bold"))
txtLbl.grid(column=0, row=0, padx=10, pady=5)

baseLbl = tk.Label(root, text="Base px:", font = ("calibri", 13))
baseLbl.grid(column=0, row=1, padx=10)
baseLbl2 = tk.Label(root, text="(*padrão 16px)", font = ("calibri", 10))
baseLbl2.grid(column=0, row=2, padx=10)

inputBaseLbl = tk.Entry(root, width=8)
inputBaseLbl.grid(column=0, row=3, padx=10, pady=5)

txtLbl = tk.Label(root, text="Digite ou copie um valor:", font = ("calibri", 13))
txtLbl.grid(column=0, row=4, padx=10, pady=5)

inputLbl = tk.Entry(root, width=15)
inputLbl.grid(column=0, row=5, padx=10)


txt = ''.ljust(40)
lbl = tk.Label(root, text=txt, foreground="#008D49", font = ("calibri", 15, "bold"))
lbl.grid(column=0, row=6, padx=10, pady=15)



conversor()
root.mainloop()

