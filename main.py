#import notification from plyer module
from plyer import notification
#import time
import time

#Use while loop to create notifications indefinetly
while(True):
    #notification
    notification.notify(
        title = "Healthy Lifestyle",
        message = "Time to drink water! 💧",
        timeout = 60
    )
    #System pause the execution of this programm for 60 minutes
    time.sleep(7200)

# 💧 Water Reminder (Healthy Lifestyle)

# A simple but effective Python script that sends desktop notifications to remind you to drink water.

### 🛠️ How to Run
# 1. Install requirements: 'pip install plyer'
# 2.Run the script: 'python main.py'
