import tkinter as tk
import ctypes
from PIL import Image, ImageTk

def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()
    
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
    # Text vidina loomine
    tekst = tk.Text(aken, wrap=tk.WORD, font=("Arial", 16, "bold"), fg="blue")
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)

    failisisu = loe_fail("tekst.txt")
    tekst.insert(tk.INSERT, failisisu)
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

if __name__ == "__main__":
    main()




