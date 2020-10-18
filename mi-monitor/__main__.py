import sys
from PyQt5.QtWidgets import QApplication
from monitor import Monitor

try:
    print('Bienvenido al Openathon VII!')
    refresh = 500
    # refresh = sys.argv[1]
    # refresh = int(refresh)
    # if refresh < 100 or refresh > 1000:
    #     raise ValueError
    # print('La frecuencia de refresco es {}'.format(refresh))
except IndexError as index_error:
    print('Por favor, tienes que indicar la velocidad de refresco como parámetro de entrada')
    sys.exit(-1)
except ValueError as value_error:
    print('{} no es un valor válido'.format(refresh))
    print('Por favor, la velocidad de refresco tiene que ser un número entre 100 y 1000')
    sys.exit(-1)

app = QApplication(sys.argv)
monitor = Monitor(refresh)

# Nos suscribimos a los cambios en los valores de la CPU
monitor.events_cpu.subscribe(
    # Cuando se publique un nuevo elemento, invocamos a la función update_cpu_data, pasándole el nuevo valor
    on_next=lambda x: monitor.update_cpu_data(x),
    # Cuando se produzca un error, lo imprimimos por consola y no actualizamos el gráfico
    on_error=lambda e: print(e),
    # Cuando se complete el observable (no se produzcan más valores) se sale de la aplicación
    on_completed=lambda: sys.exit(0)
)

monitor.events_mem.subscribe(
    # Cuando se publique un nuevo elemento, invocamos a la función update_cpu_data, pasándole el nuevo valor
    on_next=lambda x: monitor.update_memory_data(x),
    # Cuando se produzca un error, lo imprimimos por consola y no actualizamos el gráfico
    on_error=lambda e: print(e),
    # Cuando se complete el observable (no se produzcan más valores) se sale de la aplicación
    on_completed=lambda: sys.exit(0)
)

sys.exit(app.exec_())
