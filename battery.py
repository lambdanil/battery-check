# Import required modules
import os
import time
from gi.repository import Notify

# Initialize notifications
Notify.init("Power check")

# Battery low and critical values
low = 40
critical = 20

# Set current battery state
current = "normal"

# Main loop
while True:
    # Write status to file
    os.system("acpi > /tmp/battery")
    # Read status from file
    battery = open("/tmp/battery","r")
    status = battery.readline()
    # Remove status file
    os.system("rm /tmp/battery")
    # Create int(charge), which is equal to charged %
    if "Charging" in str(status):
        charge = status[21]+status[22]
    if "Discharging" in str(status):
        charge = status[24]+status[25]
    charge = int(charge)
    # Actions to do based on battery status
    if charge <= low and (current == "normal") and ("Discharging" in str(status)):
        notification = Notify.Notification.new("Warning: Battery level is low!")
        notification.show()
        time.sleep(6)
        notification.close()
        current = "low"
    elif charge <= critical and (current != "critical") and ("Discharging" in str(status)):
        notification = Notify.Notification.new("Warning: Battery level is critically low!")
        notification.show()
        time.sleep(6)
        notification.close()
        current = "critical"
    elif charge > low:
        current="normal"
    # Wait before next loop
    time.sleep(20)
    
# Close + uninitialize
battery.close()
Notify.uninit()
