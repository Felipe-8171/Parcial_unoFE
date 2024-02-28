from api.module_api import DatosAPI
from ui.module_ui import Tabla

def main():
    print("Consulta API COVID-19")
    departamento = input("Ingrese el departamento: ")
    limite = int(input("Ingrese el límite de resultados: "))

    # Crea una instancia de DatosAPI y llama al método obtener_datos
    datos_api = DatosAPI(limite, departamento)
    data = datos_api.obtener_datos()

    # Tambien verifica que los datos si se consultaron correctamente y data no esta vacío
    if data is not None:
        print("Resultados obtenidos:")
        tabla = Tabla(data)
        tabla.imprimir_datos()
    else:
        print("No se pudieron obtener datos. Por favor, inténtelo de nuevo.")

# Verifica si este archivo se está ejecutando como el programa principal
if __name__ == "__main__":
    # Llama a la función principal
    main()