
# Regex 

Regex (ou expressão regular) em Python é uma forma poderosa de buscar, verificar, extrair, substituir ou manipular padrões de texto. Ela permite definir regras para encontrar sequências específicas dentro de uma string. O Python oferece suporte a regex com o módulo **re.

---

### 📚 Funções principais do módulo **re

`Função`	        `Descrição`

**re.search()** 	Busca o padrão e retorna o primeiro match

**re.findall()**	Retorna todos os matches como lista

**re.match()**	    Verifica se o texto começa com o padrão

**re.sub()**	    Substitui partes do texto que combinam com o padrão



# Regex com Python — Guia Completo

Este documento contém **todos os termos (símbolos)** usados em **expressões regulares (regex)** com Python, com explicações claras e exemplos.

---

## Termo

- **.**

  **Explicação:**  
  Representa qualquer caractere, exceto nova linha (`\n`).

  **Exemplo:**  
  Regex: `a.b` casa com `acb`, `a#b`, mas não com `ab`.

---

## Termo

- **^**

  **Explicação:**  
  Indica o **início** da string.

  **Exemplo:**  
  Regex: `^Olá` casa com `Olá mundo`, mas não com `Oi, Olá`.

---

## Termo

- **$**

  **Explicação:**  
  Indica o **final** da string.

  **Exemplo:**  
  Regex: `mundo$` casa com `Olá mundo`, mas não com `mundo!`.

---

## Termo

- **\***

  **Explicação:**  
  Corresponde a **zero ou mais repetições** do elemento anterior.

  **Exemplo:**  
  Regex: `lo*l` casa com `ll`, `lol`, `lool`, `loooool`.

---

## Termo

- **+**

  **Explicação:**  
  Corresponde a **uma ou mais repetições** do elemento anterior.

  **Exemplo:**  
  Regex: `lo+l` casa com `lol`, `lool`, mas **não** com `ll`.

---

## Termo

- **?**

  **Explicação:**  
  Torna o caractere anterior **opcional** (zero ou uma ocorrência).

  **Exemplo:**  
  Regex: `colou?r` casa com `color` e `colour`.

---

## Termo

- **{n}**

  **Explicação:**  
  Corresponde **exatamente a n repetições** do elemento anterior.

  **Exemplo:**  
  Regex: `a{3}` casa com `aaa`, mas não com `aa` ou `aaaa`.

---

## Termo

- **{n,}**

  **Explicação:**  
  Corresponde a **n ou mais repetições**.

  **Exemplo:**  
  Regex: `a{2,}` casa com `aa`, `aaa`, `aaaa`, etc.

---

## Termo

- **{n,m}**

  **Explicação:**  
  Corresponde a **entre n e m repetições**.

  **Exemplo:**  
  Regex: `a{2,4}` casa com `aa`, `aaa`, `aaaa`.

---

## Termo

- **[]**

  **Explicação:**  
  Define um **conjunto de caracteres** aceitos.

  **Exemplo:**  
  Regex: `[aeiou]` casa com qualquer vogal.

---

## Termo

- **[^]**

  **Explicação:**  
  **Nega** um conjunto: qualquer caractere **exceto** os listados.

  **Exemplo:**  
  Regex: `[^0-9]` casa com qualquer coisa que não seja número.

---

## Termo

- **|**

  **Explicação:**  
  Representa uma **alternativa lógica** (OU).

  **Exemplo:**  
  Regex: `cachorro|gato` casa com `cachorro` ou `gato`.

---

## Termo

- **()**

  **Explicação:**  
  **Agrupa** expressões e captura o conteúdo.

  **Exemplo:**  
  Regex: `(ab)+` casa com `ab`, `abab`, `ababab`.

---

## Termo

- **\**

  **Explicação:**  
  **Caractere de escape** usado para caracteres especiais. Ex: `\.` para ponto literal.

  **Exemplo:**  
  Regex: `\.` casa com `.` no texto.

---

## Termo

- **\d**

  **Explicação:**  
  Corresponde a qualquer **dígito** (0–9). Equivale a `[0-9]`.

  **Exemplo:**  
  Regex: `\d+` casa com `2025`, `123`, etc.

---

## Termo

- **\D**

  **Explicação:**  
  Corresponde a qualquer **não-dígito**. Equivale a `[^0-9]`.

  **Exemplo:**  
  Regex: `\D+` casa com `abc`, `!@#`, etc.

---

## Termo

- **\w**

  **Explicação:**  
  Corresponde a qualquer **caractere alfanumérico** ou **underscore** (`[a-zA-Z0-9_]`).

  **Exemplo:**  
  Regex: `\w+` casa com `palavra`, `Python3`, `nome_usuario`.

---

## Termo

- **\W**

  **Explicação:**  
  Corresponde a qualquer caractere **não alfanumérico**.

  **Exemplo:**  
  Regex: `\W+` casa com `!!!`, `@#`, espaços, etc.

---

## Termo

- **\s**

  **Explicação:**  
  Corresponde a qualquer **espaço em branco** (` `, `\t`, `\n`, etc).

  **Exemplo:**  
  Regex: `\s+` casa com espaços e quebras de linha.

---

## Termo

- **\S**

  **Explicação:**  
  Corresponde a qualquer **não-espaço**.

  **Exemplo:**  
  Regex: `\S+` casa com palavras sem espaços.

---

## Termo

- **(?i)**

  **Explicação:**  
  Ativa o modo **case-insensitive** (ignora maiúsculas/minúsculas).

  **Exemplo:**  
  Regex: `(?i)python` casa com `Python`, `PYTHON`, `python`.

---

## Termo

- **(?:...)**

  **Explicação:**  
  **Agrupamento sem captura**, útil quando não precisa capturar grupos.

  **Exemplo:**  
  Regex: `(?:ab)+` casa com `ab`, `abab`, mas não captura grupos.

---

## Termo

- **(?=...)**

  **Explicação:**  
  **Lookahead positivo**: casa se for seguido de determinado padrão.

  **Exemplo:**  
  Regex: `\w+(?=@gmail\.com)` casa com `usuario` em `usuario@gmail.com`.

---

## Termo

- **(?!...)**

  **Explicação:**  
  **Lookahead negativo**: casa se **não for seguido** de determinado padrão.

  **Exemplo:**  
  Regex: `\w+(?!@gmail\.com)` casa com palavras que **não terminam** com `@gmail.com`.

---

## Termo

- **(?<=...)**

  **Explicação:**  
  **Lookbehind positivo**: casa se for **precedido** por determinado padrão.

  **Exemplo:**  
  Regex: `(?<=@)\w+` casa com `gmail` em `@gmail.com`.

---

## Termo

- **(?<!...)**

  **Explicação:**  
  **Lookbehind negativo**: casa se **não for precedido** por determinado padrão.

  **Exemplo:**  
  Regex: `(?<!@)\w+` casa com palavras **não precedidas** por `@`.

---

# Como usar regex com Python

```python
import re

texto = "Email: exemplo@gmail.com"
padrao = r"\w+@\w+\.\w+"

resultado = re.search(padrao, texto)
if resultado:
    print("Email encontrado:", resultado.group())
