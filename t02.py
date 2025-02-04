import tkinter as tk
import ctypes
from PIL import Image, ImageTk

def main():
    aken = tk.Tk()
    aken.title("tkinter ülesanded")
    aken.geometry("400x400")
    # Akna suuruse muutmise keelamine
    aken.resizable(False, True)

    # Pildi avamine ja Tkinteri jaoks ettevalmistamine
    pilt = Image.open("Norris.jpg")
    pilt = pilt.resize((200,200))
    foto = ImageTk.PhotoImage(pilt)

    # Sildi kuvamine
    label = tk.Label(aken, text="Jäck Nurris", font=("Arial", 16, "bold"), fg="blue").pack()

    # Pildi kuvamine Label abil
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

    # Tekstkast

    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

if __name__ == "__main__":
    main()




