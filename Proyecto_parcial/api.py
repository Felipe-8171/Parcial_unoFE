import pandas as pd
from sodapy import Socrata
from tabulate import tabulate

def obtener_datos(limite_registros, departamento):
    # Realiza la solicitud a la API
    try:
        # Unauthenticated client only works with public data sets . Note ’None ’
        # in place of application token , and no username or password :
        client = Socrata("www.datos.gov.co", None)

        # Realiza la solicitud a la API
        results = client.get("gt2j-8ykr", limit = limite_registros, departamento_nom = departamento)
        
        """
        Comprueba si los datos si se bajaron correctamente y results no está vacío(esto solamente es
        para pruebas y para comprobar que no hayan errores)
        
        if not results:
            print("No se encontraron datos.")
            return None
        """
        
        # Convierte los resultados en un DataFrame de Pandas
        results_df = pd.DataFrame.from_records(results)

        # Se seleccionan sólo las columnas requeridas
        columnas = ["departamento_nom","ciudad_municipio_nom","id_de_caso","edad","tipo_recuperacion","estado"]
        results_df = results_df[columnas]
        
        # Devuelve el DataFrame
        return results_df

    # Maneja excepciones(irregularidades que sucedan dentro del flujo normal del programa)
    # que puedan ocurrir durante la solicitud a la API
    except Exception as e:
        # Imprime el mensaje de error
        print("Error al obtener datos de la API:", e)
        # Retorna None para indicar el error
        return None

def imprimir_datos(data_frame):
    print(tabulate(data_frame, headers='keys', tablefmt='fancy_grid', showindex=False))
    



