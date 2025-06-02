import tkinter as tk
def main():
    aken = tk.Tk()
    aken.geometry("300x220")
    aken.title("Laenukalkulaator")
    # Funktsioon, mis kuvab sisestused
    laenusummaFrame = tk.Frame(aken)
    aastaneintressimaarFrame = tk.Frame(aken)
    laenuperioodFrame = tk.Frame(aken)
    vastus = tk.Label(aken, text="")
    def kuva_sisestus():
        try:
            laenusumma = sisestus1.get()
            aastaneintressimaar = sisestus2.get()
            laenuperiood = sisestus3.get()
            maksetearv = int(laenuperiood) * 12
            kuuintressimaar = float(aastaneintressimaar) / 100 / 12
            igakuinemakse = float(laenusumma) * (kuuintressimaar * (1 + kuuintressimaar) ** maksetearv) / ((1 + kuuintressimaar) ** maksetearv - 1)
            vahe = tk.Label(aken, text="", pady=10)
            vahe.pack()
            vastus.config(text=f"Igakuine makse: €{round(igakuinemakse,2)}", fg="black")
            vastus.pack()
        except:
            vastus.config(text="Midagi läks valesti, proovi uuesti!", fg="red")
            vastus.pack()

    # Esimene sisestusväli
    laenusummaFrame.pack(fill="x", padx=10)
    laenusummatxt = tk.Label(laenusummaFrame, text="Laenusumma (€):", pady=10)
    laenusummatxt.pack(side="left")
    sisestus1 = tk.Entry(laenusummaFrame)
    sisestus1.pack(side="left", expand=True, fill="x")
   
    # Teine sisestusväli
    aastaneintressimaarFrame.pack(fill="x", padx=10)
    aastaneintressimaartxt = tk.Label(aastaneintressimaarFrame, text="Aastane intressimäär (%):", pady=10)
    aastaneintressimaartxt.pack(side="left")
    sisestus2 = tk.Entry(aastaneintressimaarFrame)
    sisestus2.pack(side="left", expand=True, fill="x")

    laenuperioodFrame.pack(fill="x", padx=10)
    laenuperioodtxt = tk.Label(laenuperioodFrame, text="Laenuperiood (aastates):", pady=10)
    laenuperioodtxt.pack(side="left")
    sisestus3 = tk.Entry(laenuperioodFrame)
    sisestus3.pack(side="left", expand=True, fill="x")
   
    # Nupp, mis käivitab funktsiooni kuva_sisestus
    vahe = tk.Label(aken, text="")
    vahe.pack()
    pilt = tk.PhotoImage(file="pilt.png")
    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus, image=pilt, compound="left")
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()