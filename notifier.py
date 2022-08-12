from pydoc import doc
from socket import timeout
from time import sleep
from plyer import notification
import time


while True:
    notification.notify(title="TRÆNING",
        message="Kom i gang med den træning!",
        timeout = 15)
    time.sleep(120)
    
