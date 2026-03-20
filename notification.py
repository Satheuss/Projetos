import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
            title="ALERT!!!",
            message = "Take a break! It has bean an hour!",
            timeout = 3600
        )
        time.sleep(3600)

#Digite Ctrl + C no terminal para parar o Programa!
