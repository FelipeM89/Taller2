# Verificador de Cadenas Anidadas en Python (g3)

Este script en Python implementa la validación de cadenas según la siguiente gramática:


S → A 'b'
A → 'a' A 'b' | 'a' 'b


Es decir:
- La cadena debe empezar con `'a'` y terminar con `'b'`.
- La cantidad de `'a'` debe ser igual a la cantidad de `'b'`.
- Solo se aceptan cadenas anidadas como `ab`, `aabb`, `aaabbb`, etc.
- Cualquier otra cadena se rechaza.

---

## Funcionamiento

1. **Lectura del archivo**  
   El programa recibe como argumento un archivo de texto.

2. **Expresiones regulares**  
   - `re.fullmatch(r"[ab]+", linea)` asegura que la línea contiene **solo `a` y `b`**.  
   - `re.match(r"a+", linea)` obtiene el bloque inicial de `a`.  
   - `re.match(r".*?b+$", linea)` obtiene el bloque final de `b`.  
   - Se comparan las cantidades de `a` y `b` para garantizar que estén balanceadas.

3. **Validación**  
   - `acepta` → si la cadena cumple la gramática.  
   - `NO acepta` → en caso contrario.  
   - Líneas vacías se ignoran.  

---

---

## Ejecución

1. Guardar el script como `g3.py`.

2. Ejecutar en consola:
   ```bash
   python g3.py archivo.txt






