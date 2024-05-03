import threading
import queue

def tarea_dividir(q):
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        q.put("Error de división por cero en el hilo.")

errores = queue.Queue()
hilo = threading.Thread(target=tarea_dividir, args=(errores,))
hilo.start()
hilo.join()

while not errores.empty():
    print(errores.get())
