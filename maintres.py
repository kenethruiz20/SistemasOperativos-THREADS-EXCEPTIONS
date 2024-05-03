import threading
import time

def tarea():
    time.sleep(2)

hilo = threading.Thread(target=tarea)
hilo.start()
print("Hilo activo:", hilo.is_alive())
hilo.join()
print("Hilo activo después de join:", hilo.is_alive())
