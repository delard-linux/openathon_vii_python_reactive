from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout
import pyqtgraph as pg
from util import Extractor

class MonitorOld(QMainWindow):

    def __init__(self, refresh):

        super(Monitor, self).__init__()

        widget = QWidget()

        # Creamos un título para el gráfico de CPU
        self.cpu_label = QLabel()
        self.cpu_label.setText('CPU (0%)')
        # Creamos un widget para mostrar el gráfico
        self.plot_cpu = pg.PlotWidget()

        # Definimos el layout, en forma de vertical box
        vertical_box = QVBoxLayout()
        # Le indicamos que coja todo el ancho de la ventana
        vertical_box.addStretch(1)
        # Añadimos el título del gráfico
        vertical_box.addWidget(self.cpu_label)
        # Añadimos el gráfico
        vertical_box.addWidget(self.plot_cpu)

        widget.setLayout(vertical_box)

        self.setCentralWidget(widget)

        # Initialize the graph
        self.cpu_x = list(range(100))
        self.cpu = [0 for _ in range(100)]
        self.ram = [0 for _ in range(100)]
        self.extractor = Extractor()


        # Ponemos el fondo en blanco
        self.plot_cpu.setBackground('w')
        # Definimos el rango del eje Y
        self.plot_cpu.setYRange(0, 100)
        # Definimos el color de la línea
        pen = pg.mkPen(color=(120, 0, 0))
        # Creamos la línea de la CPU
        self.data_line_cpu = self.plot_cpu.plot(self.cpu_x, self.cpu, pen=pen)

        # Creamos el timer
        self.timer = QtCore.QTimer()
        # Establecemos la velocidad de refresco
        self.timer.setInterval(refresh)
        # Conectamos el método que extrae los datos de la CPU
        self.timer.timeout.connect(self.get_cpu_data)
        # Invocamos al método start, para lanazar la ejecución del timer
        self.timer.start()

        self.setWindowTitle('Mi monitor (Velocidad de refresco: {} ms)'.format(refresh))

        # self.show()

    def update_cpu_data(self, nuevo_valor):
        # Remove the first X element and add a new value
        self.cpu_x = self.cpu_x[1:]
        self.cpu_x.append(self.cpu_x[-1] + 1)

        # Remove the first CPU element and add a new value
        self.cpu = self.cpu[1:]
        self.cpu.append(nuevo_valor)

    def update_ram_data(self, nuevo_valor):
        self.ram = self.ram[1:]
        self.ram.append(nuevo_valor)

    def get_cpu_data(self):
        self.update_cpu_data(self.extractor.get_cpu_percent())

    def get_ram_data(self):
        self.update_ram_data(self.extractor.get_virtual_memory_percent())
