import tkinter as tk
from DrinksRobot import DrinksProgrammer


# Funktioner som kalder din robotkode
def lav_rom_og_cola():
    DrinksProgrammer.run_drink_program("rom_og_cola")

def lav_gin_hass():
    DrinksProgrammer.run_drink_program("gin_hass")

def lav_brandbil():
    DrinksProgrammer.run_drink_program("brandbil")

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Vælg din drink")
root.geometry("400x300")
root.configure(bg="#0f0f0f")  # Cyberpunk sort baggrund

# Label
label = tk.Label(root, text="Vælg en drink", fg="#ff00ff", bg="#0f0f0f", font=("Courier", 16, "bold"))
label.pack(pady=30)

# Rom og Cola knap
btn1 = tk.Button(root, text="Rom og Cola", command=lav_rom_og_cola,
                 fg="#39ff14", bg="#1a1a1a", activebackground="#ff00ff", activeforeground="#0f0",
                 font=("Courier", 12, "bold"), width=20, height=2)
btn1.pack(pady=10)

# Gin Hass knap
btn2 = tk.Button(root, text="Gin Hass", command=lav_gin_hass,
                 fg="#00fff7", bg="#1a1a1a", activebackground="#ff00ff", activeforeground="#0f0",
                 font=("Courier", 12, "bold"), width=20, height=2)
btn2.pack(pady=10)

# Brandbil knap
btn3 = tk.Button(root, text="Brandbil", command=lav_brandbil,
                 fg="#ff00ff", bg="#1a1a1a", activebackground="#ff00ff", activeforeground="#0f0",
                 font=("Courier", 12, "bold"), width=20, height=2)
btn3.pack(pady=10)

# Start GUI loop
root.mainloop()
