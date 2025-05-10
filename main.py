import tkinter as tk
from tkinter import font

def dodaj_u_izraz(simbol):
    trenutni = prikaz.get()
    prikaz.delete(0, tk.END)
    prikaz.insert(0, trenutni + str(simbol))

def izracunaj():
    try:
        rezultat = eval(prikaz.get())
        prikaz.delete(0, tk.END)
        prikaz.insert(0, str(rezultat))
    except Exception:
        prikaz.delete(0, tk.END)
        prikaz.insert(0, "Greška")

def obrisi():
    prikaz.delete(0, tk.END)

def obrisi_zadnji():
    trenutni = prikaz.get()
    prikaz.delete(0, tk.END)
    prikaz.insert(0, trenutni[:-1])

# Glavni prozor
root = tk.Tk()
root.title("Python Kalkulator")
root.geometry("300x450")
root.resizable(False, False)

# Stilizacija
root.configure(bg="#f0f0f0")
custom_font = font.Font(size=14)

# Prikaz rezultata
prikaz = tk.Entry(root, width=15, font=("Arial", 24), borderwidth=5, justify="right")
prikaz.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Dugmadi
dugmad = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Kreiranje dugmadi za brojeve i operatore
for (text, row, col) in dugmad:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=custom_font,
                       command=izracunaj, bg="#4CAF50", fg="white")
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=custom_font,
                       command=lambda t=text: dodaj_u_izraz(t))
    btn.grid(row=row, column=col, sticky="nsew")

# Specijalna dugmad
tk.Button(root, text='C', padx=20, pady=20, font=custom_font,
         command=obrisi, bg="#f44336", fg="white").grid(row=5, column=0, columnspan=2, sticky="nsew")
tk.Button(root, text='⌫', padx=20, pady=20, font=custom_font,
         command=obrisi_zadnji, bg="#FF9800", fg="white").grid(row=5, column=2, columnspan=2, sticky="nsew")

# Podešavanje veličine redova i kolona
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
