# Verificador de Cadenas Específicas en Python

Este script en Python valida si cada línea de un archivo de texto es exactamente `ab` o `abb`.  
Si la línea coincide con alguno de estos dos patrones, imprime `acepta`. En cualquier otro caso, imprime `NO acepta`.

---

## Funcionamiento

1. **Lectura de archivo**  
   El programa recibe como argumento un archivo de texto.

2. **Expresiones regulares**  
   - `^ab$` → acepta únicamente la cadena `"ab"`.  
   - `^abb$` → acepta únicamente la cadena `"abb"`.  

3. **Validación**  
   - Si una línea coincide con alguno de los patrones, imprime `acepta`.  
   - En caso contrario, imprime `NO acepta`.  
   - Líneas vacías se ignoran.  

---

---

##  Ejecución

1. Guardar el script como `g4.py`.

2. Ejecutar en consola:
   ```bash
   python g4.py g4.txt
---


   <img width="546" height="308" alt="Screenshot From 2025-08-19 21-46-18" src="https://github.com/user-attachments/assets/afc4c572-b127-4734-9c4a-5ca449629d2f" />





