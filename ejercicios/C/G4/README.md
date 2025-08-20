# Analizador Léxico y Sintáctico `g4.l` + `g4.y`

Este proyecto implementa un **analizador léxico y sintáctico** usando **Flex** y **Bison**.  
El lenguaje aceptado es muy simple: reconoce solo las cadenas `ab` o `abb` (cada una seguida de un salto de línea).  

---

##  Archivos

- **g4.l** → Analizador léxico (Flex).
  - Reconoce los símbolos `a`, `b`, saltos de línea (`\n`, `\r\n`) y marca cualquier otro carácter como inválido.
- **g4.y** → Analizador sintáctico (Bison).
  - Define la gramática de las cadenas aceptadas.
  - Imprime `"acepta"` cuando la línea es válida.
  - Imprime `"NO acepta"` cuando la línea contiene caracteres no permitidos o no sigue el patrón esperado.

---

##  Funcionamiento

### 1. **Reglas léxicas (`g4.l`)**
- Espacios y tabulaciones → ignorados.  
- `a` → token `'a'`.  
- `b` → token `'b'`.  
- Saltos de línea (`\n` o `\r\n`) → token `'\n'`.  
- Cualquier otro carácter → token `'x'` (inválido).  

### 2. **Reglas sintácticas (`g4.y`)**
- `input` → secuencia de líneas.  
- `line` → puede ser:
  - `'a' 'b' '\n'` → imprime `acepta`.  
  - `'a' 'b' 'b' '\n'` → imprime `acepta`.  
  - `'\n'` → línea vacía, no imprime nada.  
  - `error '\n'` → descarta el error y imprime `NO acepta`.  

---

##  Compilación

1. Generar el parser con **Bison**:
   ```bash
   bison -d g4.y

Esto crea:
- g4.tab.c → código C del parser.

- g4.tab.h → cabecera con definiciones de tokens.

2. Generar el lexer con Flex:
   ```bash
   flex g4.l

Esto crea:

lex.yy.c → código C del analizador léxico.

3. Compilar ambos con gcc:
   ```bash
   gcc g4.tab.c lex.yy.c -o g4
<img width="484" height="321" alt="image" src="https://github.com/user-attachments/assets/058a2c9b-67a7-4624-a864-e9e6dc238ae4" />

   
