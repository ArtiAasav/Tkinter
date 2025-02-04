import tkinter as tk
from PIL import Image, ImageTk

def main():
    aken = tk.Tk()
    aken.title("Tkinderi ülesanded")
    aken.geometry("200x200")
    # Akna suuruse muutmise keelamine
    aken.resizable(False, True)
   
    # Pildi avamine ja Tkinteri jaoks ettevalmistamine
    pilt = Image.open("Chuck.png")
    foto = ImageTk.PhotoImage(pilt)

    label = tk.Label(aken, text="Jack Nigris!", font=("Arial", 16, "bold"), fg='blue').pack
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

if __name__ == "__main__":
    main()




