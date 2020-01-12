# Import required modules
import subprocess
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
    # Write status to variable
    status = str(subprocess.check_output(["acpi"]))
    # Create int(charge), which is equal to charged %
    if "Charging" in str(status):
        charge = status[23]+status[24]+status[25]
    if "Discharging" in str(status):
        charge = status[26]+status[27]+status[28]
    charge = charge.replace('%','')
    charge = int(charge)
    print(charge)
    # Actions to do based on battery status
    if charge <= low and (current == "normal") and ("Discharging" in str(status)):
        notification = Notify.Notification.new("Warning: Battery level is low!")
        notification.set_urgency(2)
        notification.show()
        time.sleep(6)
        notification.close()
        current = "low"
    elif charge <= critical and (current != "critical") and ("Discharging" in str(status)):
        notification = Notify.Notification.new("Warning: Battery level is critically low!")
        notification.set_urgency(2)
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
