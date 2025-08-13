# Analizador de Cadenas Anidadas con Flex y Bison (g3.l + g3.y)

Este proyecto implementa un analizador que reconoce cadenas con un patrón **estrictamente anidado** de `a` y `b`, usando **Flex** para el análisis léxico y **Bison** para el análisis sintáctico.

---

## 📌 Funcionamiento

### 1. Análisis léxico (`g3.l`)
- Ignora espacios y tabulaciones: `[ \t]+`
- Devuelve el carácter `'a'` si encuentra `a`.
- Devuelve el carácter `'b'` si encuentra `b`.
- Reconoce saltos de línea (`(\r)?\n`) y los retorna como `'\n'`.
- Cualquier otro carácter se devuelve como `'x'` (símbolo de error).

### 2. Análisis sintáctico (`g3.y`)
- Gramática principal:
  
S → A b
A → a A b | a b

- Características:
- La cadena **siempre comienza con `a`** y termina con **`b`**.
- Permite estructuras anidadas como:
  - `ab`
  - `aabb`
  - `aaabbb`
- No permite la cadena vacía.
- Si aparece un token `'x'`, se genera un error (`YYERROR`) y se rechaza la línea.
- Procesa línea por línea:
- `acepta` si la cadena cumple la gramática.
- `NO acepta` si no la cumple.
- Líneas vacías se ignoran.

---


---

## Compilación y ejecución

1. **Generar parser con Bison**:
   
   bison -d g3.y

2. **Generar lexer con Flex**

**flex g3.l**

3.**Compilar con GCC:**

**gcc g3.tab.c lex.yy.c -o analizador3**

4.**Ejecutar:**

**./analizador3 < archivo.txt**


