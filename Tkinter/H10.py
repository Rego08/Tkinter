import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

aken = ttk.Window(themename="darkly")
aken.geometry("300x450")
aken.title("Pitsa tellimisvorm")

kullervaartus = 0
jahei = ["jah","ei"]

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

selected_suurus = ttk.IntVar(value=0)
selected_juust = ttk.IntVar(value=0)
selected_pepperoni = ttk.IntVar(value=0)
selected_seen = ttk.IntVar(value=0)

id = ttk.Label(aken, text="Kasutaja ID:", font=("Arial", 12), bootstyle="solar")
id.pack(pady=10, anchor="w", padx=10)

idEntry = ttk.Entry(aken, bootstyle="info")
idEntry.pack(fill="x", padx=10, anchor="w")

suurusLabel = ttk.Label(aken, text="Vali suurus (hind):", font=("Arial", 12), bootstyle="solar")
suurusLabel.pack(pady=10, anchor="w", padx=10)

radio_vaike = ttk.Radiobutton(aken, text="Väike (5€)", variable=selected_suurus, value=5)
radio_suur = ttk.Radiobutton(aken, text="Suur (8€)", variable=selected_suurus, value=8)
radio_pere = ttk.Radiobutton(aken, text="Pere (12€)", variable=selected_suurus, value=12)
radio_vaike.pack(anchor="w", padx=10, pady=5)
radio_suur.pack(anchor="w", padx=10, pady=5)
radio_pere.pack(anchor="w", padx=10, pady=5)

lisandidLabel = ttk.Label(aken, text="Vali lisandid (hind):", font=("Arial", 12))
lisandidLabel.pack(pady=10, anchor="w", padx=10)

radio_juust = ttk.Checkbutton(aken, text="Juust (+1€)", variable=selected_juust, onvalue=1, bootstyle="danger")
radio_pepperoni = ttk.Checkbutton(aken, text="Pepperoni (+1.5€)", variable=selected_pepperoni, onvalue=1, bootstyle="danger")
radio_seen = ttk.Checkbutton(aken, text="Seen (+1€)", variable=selected_seen, onvalue=1, bootstyle="danger")
radio_juust.pack(anchor="w", padx=10, pady=5)
radio_pepperoni.pack(anchor="w", padx=10, pady=5)
radio_seen.pack(anchor="w", padx=10, pady=5)

kuulerLabel = ttk.Label(aken, text="Vali kättetoimetamine (hind):", font=("Arial", 12))
kuulerLabel.pack(anchor="w", pady=5, padx=10)

kuller = ttk.Combobox(aken)
kuller.pack(fill="x", padx=10)

btn_message = ttk.Button(aken, text="Arvuta hind", command=show_message)
btn_message.pack(pady=20)

aken.mainloop()