import tkinter as tk

aken = tk.Tk()
aken.geometry("500x225")  # Adjusted window size for clarity
aken.title("Profiili sisestamine")
font = "Arial 10"

padx = 5
pady = 5

# Left side: Picture ("Pilt")
pilt = tk.Label(aken, text="Pilt", font=font, bg="lightgrey", width=10, height=10)
pilt.grid(row=1, column=0, rowspan=5, columnspan=4, padx=padx, pady=pady, sticky="nsew")

# Right side: Form elements
sisestatxt = tk.Label(aken, text="Palun sisesta oma andmed:", font=font)
sisestatxt.grid(row=0, column=4, columnspan=3, padx=padx, pady=pady, sticky="w")

# Name ("Nimi")
nimi = tk.Label(aken, text="Nimi", font=font)
nimi.grid(row=1, column=4, padx=padx, pady=pady, sticky="e")
nimiEntry = tk.Entry(aken)
nimiEntry.grid(row=1, column=5, padx=padx, pady=pady, sticky="w")

# Eye color ("Silmade värv")
silmavarv = tk.Label(aken, text="Silmade värv", font=font)
silmavarv.grid(row=2, column=4, padx=padx, pady=pady, sticky="e")
silmavarvEntry = tk.Entry(aken)
silmavarvEntry.grid(row=2, column=5, padx=padx, pady=pady, sticky="w")

# Height ("Pikkus")
pikkus = tk.Label(aken, text="Pikkus", font=font)
pikkus.grid(row=3, column=4, padx=padx, pady=pady, sticky="e")
pikkusEntry = tk.Entry(aken)
pikkusEntry.grid(row=3, column=5, padx=padx, pady=pady, sticky="w")

cm = tk.Label(aken, text="cm", font=font)
cm.grid(row=3, column=6, sticky="w")

# Weight ("Kaal")
kaal = tk.Label(aken, text="Kaal", font=font)
kaal.grid(row=4, column=4, padx=padx, pady=pady, sticky="e")
kaalEntry = tk.Entry(aken)
kaalEntry.grid(row=4, column=5, padx=padx, pady=pady, sticky="w")

kg = tk.Label(aken, text="kg", font=font)
kg.grid(row=4, column=6, sticky="w")

# Save button ("Salvesta")
salvesta = tk.Button(aken, text="Salvesta", font=font)
salvesta.grid(row=5, column=4, padx=padx, pady=pady, sticky="e")

# Configure grid weights to control resizing
# Left side (columns 0-3) takes 50% width, right side (columns 4-6) takes 50%
aken.grid_columnconfigure(0, weight=1)
aken.grid_columnconfigure(1, weight=1)
aken.grid_columnconfigure(2, weight=1)
aken.grid_columnconfigure(3, weight=1)
aken.grid_columnconfigure(4, weight=1)
aken.grid_columnconfigure(5, weight=1)
aken.grid_columnconfigure(6, weight=1)

for i in range(6):
    aken.grid_rowconfigure(i, weight=1)

aken.mainloop()