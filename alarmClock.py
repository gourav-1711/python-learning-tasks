import time
import datetime


def setAlarm():
    print(f"SET ALARM IN (HH:MM:SS) : ")
    running = True
    alarmTime = input()

    while running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if current_time == alarmTime:
            print("WAKE UP 🙃")
            running = False
        
        print(current_time)
        time.sleep(1)
        


if __name__ == "__main__":
    setAlarm()
