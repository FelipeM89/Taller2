import sys
import re

def procesar_archivo(ruta):
    # Creamos patrones para las cadenas válidas
    patron_ab = re.compile(r"^ab$")   # Solo "ab"
    patron_abb = re.compile(r"^abb$") # Solo "abb"

    try:
        with open(ruta, 'r') as f:
            for linea in f:
                linea = linea.strip()  # Quitamos saltos de línea y espacios
                if not linea:  # Línea vacía
                    continue

                # Verificar si la línea es válida
                if patron_ab.fullmatch(linea) or patron_abb.fullmatch(linea):
                    print("acepta")
                else:
                    print("NO acepta")

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} archivo.txt")
        sys.exit(1)

    procesar_archivo(sys.argv[1])
