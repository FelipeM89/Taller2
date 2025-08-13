
# Analizador de Cadenas Balanceadas con Flex y Bison (g2.l + g2.y)

Este proyecto implementa un analizador que reconoce cadenas con un patrón específico de **`a` y `b` balanceadas**, usando **Flex** para el análisis léxico y **Bison** para el análisis sintáctico.

---

## Funcionamiento

### 1. Análisis léxico (`g2.l`)
- Ignora espacios y tabulaciones: `[ \t]+`
- Devuelve el carácter `'a'` si encuentra `a`.
- Devuelve el carácter `'b'` si encuentra `b`.
- Reconoce saltos de línea (`(\r)?\n`) y los retorna como `'\n'`.
- Cualquier otro carácter se devuelve como `'x'` (símbolo especial para error).

### 2. Análisis sintáctico (`g2.y`)
- Regla principal: **`S → A b`**  
  Donde `A` puede contener:
  - Vacío (ε)
  - Repeticiones de `'a' A 'b'` (estructura balanceada)
- Si se encuentra un token `'x'`, se produce un error inmediatamente (`YYERROR`).
- El analizador procesa línea por línea:
  - Si la cadena cumple el patrón, imprime `acepta`.
  - Si no lo cumple, imprime `NO acepta`.
  - Líneas vacías se ignoran sin mensaje.

---


---

## Compilación y ejecución

1. **Generar parser con Bison**  
   Esto crea `g2.tab.c` y `g2.tab.h`:
  
   bison -d g2.y
2. **Generar lexer con Flex**
   Esto crea lex.yy.c:


   **flex g2.l**
3. **Compilar todo con GCC:**

   **gcc g2.tab.c lex.yy.c -o analizador2**
4. **Ejecutar el programa:**
   
   **./analizador2 < archivo.txt**

