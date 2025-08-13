# Verificador de Palíndromos Binarios en Python

Este script lee un archivo de texto y verifica si cada línea que contiene solo `0` y `1` es un **palíndromo**.  
Es la versión en Python del analizador implementado anteriormente con **Flex** y **Bison**.

---

##  Funcionamiento

1. **Lectura de archivo**  
   El programa recibe como argumento la ruta a un archivo de texto.

2. **Expresión regular**  
   Usa el patrón `r"[01]+"` para asegurarse de que la línea contenga solo ceros y unos.

3. **Verificación de palíndromo**  
   La función `es_palindromo(s)` comprueba si la cadena es igual a su inversa (`s[::-1]`).

4. **Salida**:
   - Si la línea contiene solo `0` y `1` y es un palíndromo → imprime `acepta`.
   - Si contiene solo `0` y `1` pero no es palíndromo → imprime `NO acepta`.
   - Si contiene otros caracteres o no coincide con el patrón → imprime `NO acepta`.
   - Líneas vacías se ignoran.

---

## Ejecución

1. Guardar el script en un archivo, por ejemplo `g1_python.py`.

2. Ejecutar desde terminal:
   
   python g1_python.py archivo.txt

## Ejemplo de ejecucion

<img width="549" height="382" alt="image" src="https://github.com/user-attachments/assets/e6712531-ff64-445f-bac6-10a0088d866e" />




