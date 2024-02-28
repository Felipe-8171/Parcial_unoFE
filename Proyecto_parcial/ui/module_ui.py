from tabulate import tabulate

class Tabla:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def imprimir_datos(self):
        print(tabulate(self.data_frame, headers='keys', tablefmt='fancy_grid', showindex=False))