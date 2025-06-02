import tkinter as tk
from tkinter import messagebox

aken = tk.Tk()
aken.title("Pitsa tellimisvorm")
aken.geometry("400x500")

kullervaartus = 0

def kullerilisa():
    global kullervaartus
    if kullervaartus == 0:
        kullervaartus += 3

def show_message():
    global kullervaartus
    suurus = selected_suurus.get()
    lisandid = selected_juust.get() + selected_pepperoni.get() * 1.5 + selected_seen.get()
    hindad = int(suurus) + float(lisandid) + int(kullervaartus)
    messagebox.showinfo("Pitsa hind", "Sinu pitsa hind on: "+str(hindad)+" eurot")

selected_suurus = tk.IntVar(value=0)
selected_juust = tk.IntVar(value=0)
selected_pepperoni = tk.IntVar(value=0)
selected_seen = tk.IntVar(value=0)


id = tk.Label(aken, text="Kasutaja ID:", font=("Arial", 12))
id.pack(anchor="w", pady=5, padx=10)

idEntry = tk.Entry(aken)
idEntry.pack(anchor="w", padx=10)

suurusLabel = tk.Label(aken, text="Vali suurus (hind):", font=("Arial", 12))
suurusLabel.pack(anchor="w", pady=5, padx=10)

radio_vaike = tk.Radiobutton(aken, text="Väike (5€)", font=("Arial", 12), variable=selected_suurus, value=5)
radio_suur = tk.Radiobutton(aken, text="Suur (8€)", font=("Arial", 12), variable=selected_suurus, value=8)
radio_pere = tk.Radiobutton(aken, text="Pere (12€)", font=("Arial", 12), variable=selected_suurus, value=12)
radio_vaike.pack(anchor="w", padx=10)
radio_suur.pack(anchor="w", padx=10)
radio_pere.pack(anchor="w", padx=10)

lisandidLabel = tk.Label(aken, text="Vali lisandid (hind):", font=("Arial", 12))
lisandidLabel.pack(anchor="w", pady=5, padx=10)

radio_juust = tk.Checkbutton(aken, text="Juust (+1€)", font=("Arial", 12), variable=selected_juust, onvalue=1)
radio_pepperoni = tk.Checkbutton(aken, text="Pepperoni (+1.5€)", font=("Arial", 12), variable=selected_pepperoni, onvalue=1)
radio_seen = tk.Checkbutton(aken, text="Seen (+1€)", font=("Arial", 12), variable=selected_seen, onvalue=1)
radio_juust.pack(anchor="w", padx=10)
radio_pepperoni.pack(anchor="w", padx=10)
radio_seen.pack(anchor="w", padx=10)

kuulerLabel = tk.Label(aken, text="Vali kättetoimetamine (hind):", font=("Arial", 12))
kuulerLabel.pack(anchor="w", pady=5, padx=10)

kuller = tk.Button(aken, text="Kuller (+3€)", font=("Arial", 12), command=kullerilisa)
kuller.pack(pady=5, padx=10, anchor="w")

btn_message = tk.Button(aken, text="Arvuta hind", command=show_message, font=("Arial", 12))
btn_message.pack(pady=30)

aken.mainloop()