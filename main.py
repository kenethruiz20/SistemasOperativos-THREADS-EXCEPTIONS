import threading

def tarea_dividir():
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Error en el hilo: no se puede dividir por cero.")

# Creación y ejecución del hilo
hilo = threading.Thread(target=tarea_dividir)
hilo.start()
hilo.join()
