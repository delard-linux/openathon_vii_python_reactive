"""
Comentario de modulo para que detecte el cambio
AQUI METO UN CAMBIO!! para que desde created_remotelly sobre main desde el VSCode
esto es un cambio desde 2nd_created_remotelly sobre main
"""  
import pyqtgraph as pg
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from rx.subject import Subject

from util import Extractor

class Monitor(QMainWindow):
    """
    Clase Monitor de momento sin programacion reactiva
    """
    def __init__(self, refresh):
        """
        Para que salte conflicto
        """
        super(Monitor, self).__init__()

        # SE incluye el observable
        self.events_cpu = Subject()
        self.events_mem = Subject()

        widget = QWidget()

        # Graph Component
        self.cpu_label = QLabel()
        self.cpu_label.setText('CPU (0%)')
        self.plot_cpu = pg.PlotWidget()

        self.memory_label = QLabel()
        self.memory_label.setText('Memoria (0%)')
        self.plot_memory = pg.PlotWidget()

        vertical_box = QVBoxLayout()
        vertical_box.addStretch(1)
        vertical_box.addWidget(self.cpu_label)
        vertical_box.addWidget(self.plot_cpu)
        vertical_box.addWidget(self.memory_label)
        vertical_box.addWidget(self.plot_memory)

        widget.setLayout(vertical_box)

        self.setCentralWidget(widget)

        # Initialize the Graph
        self.cpu_x = list(range(100))
        self.memory_x = list(range(100))
        self.memory = [0 for _ in range(100)]
        self.cpu = [0 for _ in range(100)]

        # Configure the Graph
        self.plot_cpu.setBackground('w')
        self.plot_cpu.setYRange(0, 100)
        self.plot_memory.setBackground('w')
        self.plot_memory.setYRange(0, 100)

        # Data of the memory
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line_memory = self.plot_memory.plot(self.memory_x, self.memory, pen=pen)

        # Data of the CPU
        pen = pg.mkPen(color=(120, 0, 0))
        self.data_line_cpu = self.plot_cpu.plot(self.cpu_x, self.cpu, pen=pen)

        self.extractor = Extractor()

        # Refresh the data
        self.timer = QtCore.QTimer()
        self.timer.setInterval(refresh)
        self.timer.timeout.connect(self.get_memory_data)
        self.timer.timeout.connect(self.get_cpu_data)
        self.timer.start()

        self.setWindowTitle('Monitor (Velocidad de refresco: {} ms)'.format(refresh))

        self.show()

    def update_memory_data(self, event):
        """
        Actualiza la información del gráfico de memoria
        Esta linea se ha metido para ver diferencias !!
        :return:
        """
        # Remove the first X element and add a new value
        self.memory_x = self.memory_x[1:]
        self.memory_x.append(self.memory_x[-1] + 1)

        # Remove the first CPU element and add a new value
        self.memory = self.memory[1:]
        self.memory.append(event)
        self.data_line_memory.setData(self.memory_x, self.memory)

        self.memory_label.setText('Memoria ({}%)'.format(event))

    def update_cpu_data(self, event):
        """
        Actualiza la información del gráfico de CPU
        :return:
        """
        # Remove the first X element and add a new value
        self.cpu_x = self.cpu_x[1:]
        self.cpu_x.append(self.cpu_x[-1] + 1)

        # Remove the first CPU element and add a new value
        self.cpu = self.cpu[1:]
        self.cpu.append(event)
        self.data_line_cpu.setData(self.cpu_x, self.cpu)

        self.cpu_label.setText('CPU ({}%)'.format(event))

    def get_cpu_data(self):
        """
        Método que recupera el valor de la CPU y envía un evento de forma reactiva
        """
        # Publica un nuevo valor en el Observable de valores de la CPU
        self.events_cpu.on_next(self.extractor.get_cpu_percent())

    def get_memory_data(self):
        """
        Método que recupera el valor de la memoria y envía un evento de forma reactiva
        """
        # Publica un nuevo valor en el Observable de valores de la CPU
        self.events_mem.on_next(self.extractor.get_virtual_memory_percent())

