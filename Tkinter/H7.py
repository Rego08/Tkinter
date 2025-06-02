import tkinter as tk

aken = tk.Tk()
aken.title("Isikukoodi validaator")
aken.geometry("300x200")

def naita():
    synniaegtxt.config(text=f"Sünniaeg: ")
    sugutxt.config(text=f"Sugu: ")
    global text
    sugu = text[0]
    aasta = str(text[1])+str(text[2])
    
    if int(sugu) == 1 or int(sugu) == 3 or int(sugu) == 5 or int(sugu) == 7:
        sugutxt.config(text=f"Sugu: mees")
    elif int(sugu) == 2 or int(sugu) == 4 or int(sugu) == 6 or int(sugu) == 8:
        sugutxt.config(text=f"Sugu: naine")
    
    if int(sugu) == 1 or int(sugu) == 2:
        sajand = 1800
        synniaasta = sajand + int(aasta)
    elif int(sugu) == 3 or int(sugu) == 4:
        sajand = 1900
        synniaasta = sajand + int(aasta)
    elif int(sugu) == 5 or int(sugu) == 6:
        sajand = 2000
        synniaasta = sajand + int(aasta)
    elif int(sugu) == 7 or int(sugu) == 8:
        sajand = 2100
        synniaasta = sajand + int(aasta)
    
    # Vanus
    paev = str(text[5])+str(text[6])
    kuu = str(text[3])+str(text[4])
    synniaegtxt.config(text=f"Sünniaeg: {paev}.{kuu}.{synniaasta}")

def clear():
    synniaegtxt.config(text=f" ")
    sugutxt.config(text=f" ")

def valideeriTeksti(*args):
    global text
    text = entry_var.get()
    if len(text) == 11:
        validation_label.config(text="")
        isikukood = entry_var.get()
        synniaegtxt = tk.Label(aken, text=f"Sünniaeg: ", font=("Arial"), fg="green")
        sugutxt = tk.Label(aken, text=f"Sugu: ", fg="green", font=("Arial"))
        naita()
    else:
        clear()
        validation_label.config(text="Isikukood peab olema 11 märki pikk", fg="red")

label = tk.Label(aken, text="Isikukood", font=("Arial", 15))
label.pack(pady=10)

entry_var = tk.StringVar()
entry_var.trace_add("write", valideeriTeksti)

entry = tk.Entry(aken, textvariable=entry_var, width=30)
entry.pack()

validation_label = tk.Label(aken, text="Isikukood peab olema 11 märki pikk", fg="red")
validation_label.pack()

synniaegtxt = tk.Label(aken, text="", font=("Arial"), fg="green")
sugutxt = tk.Label(aken, text="", fg="green", font=("Arial"))
synniaegtxt.pack(side="bottom", pady=10)
sugutxt.pack(side="bottom")

aken.mainloop()