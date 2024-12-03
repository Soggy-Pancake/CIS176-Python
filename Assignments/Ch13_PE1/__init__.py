import tkinter as tk

def assignmentName() -> str:
    return "Chapter 13 (Name and Address)"

def toggleInfo(infoLabel):
    global infoVisible

    infoVisible = infoVisible == False
    if(infoVisible):
        infoLabel.place(x=40,y=20) 
    else:
        infoLabel.place_forget()
    

infoVisible = False

def main():
    window =tk.Tk()
    window.config(width=180,height=140)

    window.title("Python gui")
    
    infoLabel = tk.Label(window, text="Totally RealName\n1234 Brain Lane\nMind city, AB", justify="center", anchor="center")

    infoBtn = tk.Button(window, text="Show Info", command=lambda: toggleInfo(infoLabel))
    infoBtn.place(x=40,y=100)

    exitBtn = tk.Button(window, text="Exit", command=lambda: window.destroy())
    exitBtn.place(x=110,y=100)

    window.mainloop()

if __name__ == "__main__":
    assignmentName()
    main()