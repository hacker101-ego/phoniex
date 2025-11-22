print(r"""
      _                      _      
  _ __ | |__   ___   ___ _ __ ()  __
 | '_ | '_  / _  / _  '_ |  / /
 | |) | | | | () |  __/ | | | |>  < 
 | ./|| ||/ ___|| ||//\
 |_|
            /|       |
 /  |       |  \
|         /    |
|   /      /  |
|   |     |  / |
|  _/^/_ / |
|    --//--    |
 _       /  _/
   __  |  __/
       _ /
     _/   _   
    / /|   
     /  |    
      / v \
      ~ PHONIEX ~ (Phoenix Bird)
""")

import subprocess

class Phoniex:
    def _init_(self, name, version, author):
        self.name = name
        self.version = version
        self.author = author

    def connect(self, ip, port):
        print(f"Connecting to {ip}:{port}...")
        # Actual connection code goes here (e.g., using sockets)
        print("Connected!")

    def execute_command(self, command):
        print(f"Executing command: {command}...")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout if result.stdout else result.stderr
        except Exception as e:
            output = str(e)
        print(f"Command Output:{output}")
        return output

    def remote_screen_view(self):
        print("Starting remote screen view...")
        print("[Simulated screen streaming]")

    def hardware_control(self, device_component, action):
        allowed_components = ["camera", "microphone", "gps"]
        if device_component.lower() not in allowed_components:
            print("Hardware component not supported.")
            return
        print(f"Performing '{action}' on {device_component} hardware...")
        print(f"Action '{action}' executed on {device_component} successfully.")
     