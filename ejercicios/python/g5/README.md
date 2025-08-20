# Verificador de Balanceo de `a` y `b` (g5.py)

Este script en Python valida cadenas de caracteres formadas únicamente por `a` y `b`.  
La regla que sigue es:  

- La cadena debe **empezar con `a` y terminar con `b`**.  
- La cantidad de `a` iniciales debe ser igual a la cantidad de `b` finales.  
- No se permiten otros caracteres.  

---

## Funcionamiento

1. **Lectura del archivo**  
   El programa recibe un archivo de texto como argumento. Cada línea del archivo es analizada.

2. **Validaciones con expresiones regulares**  
   - `re.fullmatch(r"[ab]+", linea)` → asegura que la cadena solo tenga `a` y `b`.  
   - `

