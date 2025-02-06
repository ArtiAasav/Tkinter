import tkinter as tk

def main():
    aken = tk.Tk()
    aken.title("Tkinderi ülesanded")
    aken.geometry("400x200")
   
    font = "Arial 10"
    padx = 5
    pady = 5

    # Loo sildid, mis näitavad lahtri koordinaate
    for row in range(6):
        for column in range(4):
            
            nupp_00 = tk.Label(aken, text="Pilt", font=font, bg="silver")
            nupp_00.grid(row=1, column=0, rowspan=5, columnspan=2, padx=padx, pady=pady, sticky="nsew")

            label1 = tk.Label(aken, text="Palun sisestage oma andmed:", font=font)
            label1.grid(row=0, column=2, columnspan=2, padx=padx, pady=pady, sticky="nsew")
        
            label2 = tk.Label(aken, text="Nimi", font=font)
            label2.grid(row=1, column=2, padx=padx, pady=pady, sticky="nsew")

            sisestus1 = tk.Entry(aken)
            sisestus1.grid(row=1, column=3, padx=padx, pady=pady, sticky="nsew")

            label3 = tk.Label(aken, text="Silmade värv", font=font)
            label3.grid(row=2, column=2, padx=padx, pady=pady, sticky="nsew")

            sisestus2 = tk.Entry(aken)
            sisestus2.grid(row=2, column=3, padx=padx, pady=pady, sticky="nsew")

            label4 = tk.Label(aken, text="Pikkus", font=font)
            label4.grid(row=3, column=2, padx=padx, pady=pady, sticky="nsew")

            sisestus3 = tk.Entry(aken)
            sisestus3.grid(row=3, column=3, padx=padx, pady=pady, sticky="nsew")

            label5 = tk.Label(aken, text="Kaal", font=font)
            label5.grid(row=4, column=2, padx=padx, pady=pady, sticky="nsew")

            sisestus4 = tk.Entry(aken)
            sisestus4.grid(row=4, column=3, padx=padx, pady=pady, sticky="nsew")

            label6 = tk.Label(aken, text="cm", font=font)
            label6.grid(row=3, column=4, padx=padx, pady=pady, sticky="nsew")

            label7 = tk.Label(aken, text="kg", font=font)
            label7.grid(row=4, column=4, padx=padx, pady=pady, sticky="nsew")

            nupp_01 = tk.Button(aken, text="Salvesta", font=font)
            nupp_01.grid(row=5, column=2, padx=padx, pady=pady, sticky="nsew")

    

    # Nuppude seadistamine
    # aken.grid_rowconfigure(0, weight=1)
    # aken.grid_rowconfigure(1, weight=1)
    # aken.grid_rowconfigure(2, weight=1)
    # aken.grid_rowconfigure(3, weight=1)
    # aken.grid_rowconfigure(4, weight=1)
    # aken.grid_rowconfigure(5, weight=1)
    aken.grid_columnconfigure(0, weight=1)
    aken.grid_columnconfigure(1, weight=1)
    aken.grid_columnconfigure(2, weight=1)
    aken.grid_columnconfigure(3, weight=1)
    aken.grid_columnconfigure(4, weight=1)
    aken.grid_columnconfigure(5, weight=1)




    aken.mainloop()

if __name__ == "__main__":
    main()