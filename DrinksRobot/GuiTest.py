import tkinter as tk
from DrinksProgrammer import DrinksProgrammer
from RobotComms import RobotComms
from RobotState import RobotState
from PauseFisk import PauseFisk
import threading
import time
import socket

robot_ip = "192.168.0.101"
comms = RobotComms(robot_ip)
drinks_programmer = DrinksProgrammer(comms)

# GUI setup
root = tk.Tk()
root.title("Drink Robot")
root.geometry("400x400")

# ---- Funktion til at enable/disable knapper ----
def set_buttons_state(state):
    btn1.config(state=state)
    btn2.config(state=state)
    btn3.config(state=state)

# ---- Tjek om program er færdigt ----
def monitor_program():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((robot_ip, comms.DASHBOARD_PORT))
            s.recv(1024)
            s.sendall(b"is program running\n")
            response = s.recv(1024).decode().strip()
            s.close()

            if "false" in response.lower():
                # Robot er færdig – enable knapper igen
                set_buttons_state("normal")
                break
        except Exception as e:
            print(f"Fejl ved tjek af programstatus: {e}")
            break
        time.sleep(1)

def show_popup():
    # Hent hovedvinduets position & størrelse
    root.update_idletasks()
    x = root.winfo_x()
    y = root.winfo_y()
    width = root.winfo_width()
    height = root.winfo_height()

    popup = tk.Toplevel(root)
    popup.title("Vent venligst")
    popup.geometry(f"{width}x{height}+{x}+{y}")  # Match størrelse & position
    popup.attributes("-topmost", True)  # Always on top
    popup.grab_set()  # Disable klik udenfor popup

    # Label i midten
    label = tk.Label(popup, text="Robotten kører program...\nVent venligst", font=("Arial", 16))
    label.place(relx=0.5, rely=0.5, anchor="center")

    # Luk efter 7 sekunder
    popup.after(7000, popup.destroy)

# ---- Funktioner til knapper ----
def run_drink(drink):
    print(f"Kører {drink}")
    show_popup()
    drinks_programmer.run_program(drink)
    # Start monitor thread
    monitor_thread = threading.Thread(target=monitor_program)
    monitor_thread.start()

# ---- Knapper ----
btn1 = tk.Button(root, text="Rom og Cola", command=lambda: run_drink("rom_og_cola"), width=25, height=3)
btn1.pack(pady=20)

btn2 = tk.Button(root, text="Gin Hass", command=lambda: run_drink("gin_hass"), width=25, height=3)
btn2.pack(pady=20)

btn3 = tk.Button(root, text="Brandbil", command=lambda: run_drink("brandbil"), width=25, height=3)
btn3.pack(pady=20)

exit_btn = tk.Button(root, text="Afslut", command=root.destroy, width=25, height=3, bg="red", fg="white", font=("Arial", 14))
exit_btn.pack(pady=20)

# ---- PauseFisk monitor i baggrunden ----
pause = PauseFisk(comms)
idle_thread = threading.Thread(target=pause.monitor_idle)
idle_thread.daemon = True
idle_thread.start()



# ---- Start GUI ----
root.mainloop()
