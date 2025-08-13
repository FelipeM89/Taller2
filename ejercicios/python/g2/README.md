# Verificador de Gramática Balanceada en Python (g2)

Este script lee un archivo de texto y valida si cada línea cumple la siguiente gramática:

S → A 'b'
A → ε | 'a' A 'b'


Además, cualquier cadena que contenga el carácter `x` es rechazada inmediatamente.

---

##  Funcionamiento

1. **Lectura de archivo**  
   El programa recibe como argumento la ruta a un archivo de texto.

2. **Reglas de validación**  
   - La cadena debe terminar con `'b'`.
   - El contenido antes del último `'b'` (`A`) puede estar vacío o seguir la estructura `'a' A 'b'`.
   - No puede contener `x`.
   - Se procesa usando una función recursiva que implementa directamente la gramática.

3. **Salida**:
   - `acepta` → si la cadena cumple la gramática.
   - `NO acepta` → si no la cumple o contiene `x`.
   - Líneas vacías se ignoran.

---

---

## Ejecución

1. Guardar el script como `g2.py`.

2. Ejecutar:
   
   python g2.py archivo.txt

## Ejemplo de ejecucion 

<img width="513" height="362" alt="Screenshot From 2025-08-13 13-10-27" src="https://github.com/user-attachments/assets/85f8197e-77e8-463e-a9c6-e2b215c958e1" />





