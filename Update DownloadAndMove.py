import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Clase Event Hanlder 
class FileEventHandler(FileSystemEventHandler):

    #1_on_created

    #2_on_deleted

    #3_on_modified

    #4_on_moved

        


# Inicia clase Event Handler 
event_handler = FileEventHandler()

# Inicia Observer
observer = Observer()

# Programa the Observer
observer.schedule(event_handler, from_dir, recursive=True)


#Comienza el Observer
observer.start()


#5 Escribe una excepción para keyboardInterrupt

while True:
    time.sleep(2)
    print("ejecutando...")


