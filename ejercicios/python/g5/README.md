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
   - `re.match(r"a+", linea)` → cuenta las `a` consecutivas desde el inicio.  
   - `re.match(r".*?b+$", linea)` → detecta las `b` consecutivas al final.  

3. **Condiciones**  
   - Debe empezar con `a` y terminar con `b`.  
   - Número de `a` iniciales = número de `b` finales.  
   - Si cumple → imprime `acepta`.  
   - Si no cumple → imprime `NO acepta`.  

---

---

## Ejecución

1. Guardar el script como `g5.py`.  
2. Ejecutar en consola:  

   ```bash

   python g5.py archivo.txt
---
   <img width="520" height="481" alt="Screenshot From 2025-08-19 21-58-39" src="https://github.com/user-attachments/assets/3f9dd789-98c9-46c0-9fbb-fcd2e6134162" />



