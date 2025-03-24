import socket

#klasse til robot kommandor
class RobotComms:
    def __init__(self, robot_ip):
        self.robotIP = robot_ip
        self.DASHBOARD_PORT = 29999
        self.SECONDARY_PORT = 30002

    def load_and_run_program(self, program_name):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((self.robotIP, self.DASHBOARD_PORT))
            s.recv(1024)
            # Load fra /programs
            s.sendall(f"load {program_name}\n".encode('utf-8'))
            print(s.recv(1024).decode().strip())
            # Play
            s.sendall(b"play\n")
            print(s.recv(1024).decode().strip())
            s.close()
            print(f"{program_name} loaded and running!")
        except Exception as e:
            print(f"Fejl ved load/run: {e}")

    def send_pause_script(self, script_file):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((self.robotIP, self.SECONDARY_PORT))
            with open(script_file, "r") as f:
                script = f.read()
            s.sendall(script.encode('utf-8'))
            s.close()
            print("Pause script sendt.")
        except Exception as e:
            print(f"Fejl ved pause script: {e}")
