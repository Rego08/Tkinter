import tkinter as tk

aken = tk.Tk()
aken.title("Raadionuppude näide")

def show_selection():
    print("Valitud värv:", selected_color.get())

# StringVar, mis hoiab valitud värvi nime
selected_color = tk.StringVar(value="red")

# Loome raadionupud
radio_red = tk.Radiobutton(aken, text="punane", variable=selected_color, value="red")
radio_green = tk.Radiobutton(aken, text="roheline", variable=selected_color, value="green")
radio_blue = tk.Radiobutton(aken, text="sinine", variable=selected_color, value="blue")
radio_red.pack()
radio_green.pack()
radio_blue.pack()

btn_confirm = tk.Button(aken, text="Kinnita valik", command=show_selection)
btn_confirm.pack()

aken.mainloop()