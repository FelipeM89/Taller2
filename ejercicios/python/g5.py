# g5.py
import sys

def acepta(linea):
    # Quitamos espacios, tabs y \r como en el .l
    linea = linea.replace(" ", "").replace("\t", "").replace("\r", "").strip("\n")

    # Implementa la gramática:
    # S -> A 'b'
    # A -> 'a' | A 'a' 'b'
    if not linea:
        return False
    if linea[0] != 'a':
        return False
    
    i = 1
    while i < len(linea) - 1:
        if linea[i] == 'a' and i + 1 < len(linea) and linea[i+1] == 'b':
            i += 2
        else:
            return False
    return linea[-1] == 'b'


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} archivo.txt")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        for linea in f:
            if acepta(linea):
                print("acepta")
            else:
                print("NO acepta")
