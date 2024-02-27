from api import obtener_datos, imprimir_datos

def mostrar_resultados():
    print("Consulta API COVID-19")
    departamento = input("Ingrese el departamento: ")
    limite = int(input("Ingrese el límite de resultados: "))

    # Llama a la función del módulo de API para obtener los datos
    data = obtener_datos(limite, departamento)

    # Tambien verifica que los datos si se consultaron correctamente y data no esta vacío
    if data is not None:
        print("Resultados obtenidos:")
        imprimir_datos(data)
    else:
        print("No se pudieron obtener datos. Por favor, inténtelo de nuevo.")






    