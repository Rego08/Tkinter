import tkinter as tk

def main():
    def varv(color):
        txt.config(text=color)

    aken = tk.Tk()
    aken.geometry("400x100")

    button_frame = tk.Frame(aken)
    button_frame.pack(side="top", fill="both", expand=True)

    text_frame = tk.Frame(aken)
    text_frame.pack(side="bottom", fill="both", expand=True)

    # Label at the bottom
    txt = tk.Label(text_frame, text="", font=("Arial", 20))
    txt.pack(fill="both", expand=True)

    # Buttons
    nupp1 = tk.Button(button_frame, bg="blue", command=lambda: varv("Sinine"))
    nupp2 = tk.Button(button_frame, bg="green", command=lambda: varv("Roheline"))
    nupp3 = tk.Button(button_frame, bg="yellow", command=lambda: varv("Kollane"))
    nupp4 = tk.Button(button_frame, bg="orange", command=lambda: varv("Oranž"))
    nupp5 = tk.Button(button_frame, bg="red", command=lambda: varv("Punane"))

    nupp1.pack(fill="both", side="right", expand=True)
    nupp2.pack(fill="both", side="right", expand=True)
    nupp3.pack(fill="both", side="right", expand=True)
    nupp4.pack(fill="both", side="right", expand=True)
    nupp5.pack(fill="both", side="right", expand=True)

    aken.mainloop()

if __name__ == "__main__":
    main()
