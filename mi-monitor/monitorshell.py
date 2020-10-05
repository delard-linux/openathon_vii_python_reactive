import time
from util import Extractor

class MonitorShell():

    def __init__(self, refresh):
        self.cpu = [0 for _ in range(100)]
        self.ram = [0 for _ in range(100)]
        self.extractor = Extractor()

        while True:
            self.get_cpu_data()
            self.get_ram_data()
            print("CPU: {}".format(self.cpu))
            print("RAM: {}".format(self.ram))
            print("--------------------")
            time.sleep(refresh/1000)

    def update_cpu_data(self, nuevo_valor):
        # Elimina el primer valor de la lista
        self.cpu = self.cpu[1:]
        self.cpu.append(nuevo_valor)

    def update_ram_data(self, nuevo_valor):
        # Elimina el primer valor de la lista
        self.ram = self.ram[1:]
        self.ram.append(nuevo_valor)

    def get_cpu_data(self):
        self.update_cpu_data(self.extractor.get_cpu_percent())

    def get_ram_data(self):
        self.update_ram_data(self.extractor.get_virtual_memory_percent())

# MonitorShell(1000)
