# Analizador de Palíndromos con Flex y Bison

Este proyecto implementa un analizador que reconoce cadenas formadas únicamente por `0` y `1` y determina si son **palíndromos**.  
Se compone de:
- **`g1.l`** → Analizador léxico (Flex)
- **`g1.y`** → Analizador sintáctico (Bison)

---

##  Funcionamiento

### 1. Análisis léxico (`g1.l`)
- Detecta secuencias de `0` y `1` usando la expresión regular `[01]+`.
- Copia la cadena encontrada en el buffer global `buffer`.
- Devuelve el token `CADENA` al analizador sintáctico.
- Ignora espacios, tabulaciones y otros caracteres.
- Maneja saltos de línea para indicar fin de entrada de una cadena.

### 2. Análisis sintáctico (`g1.y`)
- Recibe el token `CADENA` y el contenido de `buffer`.
- Llama a la función `es_palindromo` para verificar si la cadena es igual al revés.
- Imprime:
  - `acepta` si es palíndromo.
  - `NO acepta` si no lo es.
- Permite múltiples líneas de entrada, procesando cada cadena por separado.

---

---

## Compilación y ejecución

1. **Generar parser con Bison**  
   Esto crea `g1.tab.c` y `g1.tab.h`:
   ```bash
   bison -d g1.y



