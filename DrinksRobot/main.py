from RobotComms import RobotComms
from PauseFisk import PauseFisk
from DrinksProgrammer import DrinksProgrammer
import threading

robot_ip = "192.168.0.101"
comms = RobotComms(robot_ip)

# Start PauseFisk i baggrundstråd
pause = PauseFisk(comms)
idle_thread = threading.Thread(target=pause.monitor_idle)
idle_thread.daemon = True
idle_thread.start()

# Start drinks-menu
drinks = DrinksProgrammer(comms)
drinks.menu()
