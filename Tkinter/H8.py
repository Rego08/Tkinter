import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import os
from PIL import Image, ImageOps

def open_directory():
    pilt = filedialog.askopenfiles()
    if pilt:
        dir_label.config(text=f"Valitud kaust: {pilt}")
    else:
        dir_label.config(text="Pilti ei valitud.")

def create_thumbnails(source_dir, thumb_dir, size=(350, 350)):
    # Kontrolli, kas thumb kataloog on olemas, kui ei ole, siis loo see
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)
    # Kõikide JPG failide leidmine kataloogis
    nimi = 0 
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".jpg"):
            nimi += 1
            img_path = os.path.join(source_dir, filename)
            img = Image.open(img_path)

            # Värvisügavuse muutmine
            img = img.convert('L')
           
            # Pisipildi loomine
            thumb_img = ImageOps.fit(img, size, centering=(0.5, 0.5))
            img.close()
            
            # Pisipildi salvestamine
            thumb_path = os.path.join(thumb_dir,str(nimi)+".jpg")
            thumb_img.save(thumb_path, "JPEG")
    
            print(f"Pisipilt salvestatud: {thumb_path}")


aken = tk.Tk()
aken.title("Peamine aken")
aken.geometry("450x400")

label = tk.Label(aken, text="Pildi suurus 200x200", font=("Arial", 20))
label.pack()

piltFrame = tk.Frame(aken, bg="white", padx=200, pady=100)
piltFrame.pack()

open_button = tk.Button(aken, text="Vali failid", command=open_directory)
open_button.pack(pady=10)

save_button = tk.Button(aken, text="Salvesta pildid", command=save_directory)
save_button.pack(pady=10)

dir_label = tk.Label(piltFrame, text="")
dir_label.pack(pady=10)

# Kasuta funktsiooni
source_directory = 'img/yl_pildid'
thumb_directory = 'img/thumb'
create_thumbnails(source_directory, thumb_directory)

aken.mainloop()