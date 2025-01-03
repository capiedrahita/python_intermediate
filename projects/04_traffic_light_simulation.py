
# Traffic Light Simulation
# This program simulates the behavior of a traffic light using loops.

import time

# Step 1: Define the traffic light sequence
lights = ["Green", "Yellow", "Red"]

print("Traffic Light Simulation. Press Ctrl+C to stop.")

# Step 2: Simulate the traffic light
try:
    while True:
        for light in lights:
            if light == "Green":
                print(f"{light} light is ON. (Duration: 5 seconds)")
                time.sleep(5)
            elif light == "Yellow":
                print(f"{light} light is ON. (Duration: 2 seconds)")
                time.sleep(2)
            elif light == "Red":
                print(f"{light} light is ON. (Duration: 7 seconds)")
                time.sleep(7)
except KeyboardInterrupt:
    print("Traffic light simulation stopped.")
