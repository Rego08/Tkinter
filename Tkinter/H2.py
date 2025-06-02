import tkinter as tk
from img import Image, ImageTk

def kuva_pilt(aken, failinimi, laius, korgus):
    pilt = Image.open(failinimi)
    pilt = pilt.resize((laius, korgus))
    foto = ImageTk.PhotoImage(pilt)
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    aken = tk.Tk()
    aken.title("Ülessanne 2")
    aken.geometry("400x400")
    aken.resizable(False, False)
    
    label = tk.Label(aken,text="Chuck Norris",font=("Arial", 16, "bold"),fg="blue",padx=20,pady=10,anchor="w")
    
    label.pack()

    kuva_pilt(aken, "dickpic.jpg", 200, 200)

    tekst = tk.Text(aken, wrap=tk.WORD)
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)

    tekst.tag_configure('center_bold', justify='center', font=('Arial', 12, 'bold'))
    failisisu = loe_fail("text.txt")
    tekst.insert(tk.INSERT, failisisu)

    aken.mainloop()

if __name__ == "__main__": main()