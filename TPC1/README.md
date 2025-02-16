# TPC1: Manipulação de Strings em Python

Este projeto contém diversas funções para a **manipulação de strings**. Para além disso, contém um **menu interativo** para que estas possam ser testadas individualmente, havendo também a possibilidade de realizar **testes automáticos**.

---

## **Lista de Funções Implementadas**

Em seguida apresentam-se todas as funções implementadas no projeto, em conjunto com uma breve descrição e exemplo.

---

### 1. **`reverse(string)`:**
🔹 **Descrição:** Inverte uma string.  
🔹 **Exemplo:** `reverse("hello")` retorna `"olleh"`

### 2. **`find_a(string)`:**
🔹 **Descrição:** Conta o número de caratéres "a" ou "A" na string.  
🔹 **Exemplo:** `find_a("BAnana")` retorna `3`

### 3. **`vowels(string)`:**
🔹 **Descrição:** Conta o número de vogais numa string.
🔹 **Exemplo:** `vowels("Olarilole)` retorna `5`

### 4. **`lower(string)`:**
🔹 **Descrição:** Converte a string para minúsculas.  
🔹 **Exemplo:** `lower("Hello")` retorna `"hello"`

### 5. **`upper(string)`:**
🔹 **Descrição:** Converte a string para maiúsculas.  
🔹 **Exemplo:** `upper("Hello")` retorna `"HELLO"`

### 6. **`capicua(string)`:**
🔹 **Descrição:** Verifica se a string dada é uma capicua, reconhecendo tanto uma única palavra ou uma frase.  
🔹 **Exemplo 1:** `capicua("Ana"))` retorna `True`
🔹 **Exemplo 2:** `capicua("Luz Azul")` retorna `True`

### 7. **`balanceadas(s1, s2)`:**
🔹 **Descrição:** Verifica se as duas strings estão balanceadas, ou seja, se todos os caracteres da primeira string estão presentes na segunda.  
🔹 **Exemplo:** `balanceadas("Luz AZual", "zzaul")` retorna `True`

### 8. **`ocorrencias(s1, s2)`:**
🔹 **Descrição:** Conta quantas vezes a primeira string ocorre na segunda.  
🔹 **Exemplo:** `ocorrencias("ola", "ola adeus, ola bom dia")` retorna `2`

### 9. **`anagrama(s1, s2)`:**
🔹 **Descrição:** Verifica se as duas strings são anagramas entre si.  
🔹 **Exemplo 1:** `anagrama("listen", "silent"),` retorna `True`
🔹 **Exemplo 2:** `anagrama("hello", "world"),` retorna `False`

### 10. **`classes_anagramas(list)` e `tabela_anagramas(dici)`:**
🔹 **Descrição:** Em conjunto, permitem a criação de uma tabela de classes de anagramas. A primeira função cria um dicionário das respetivas classes de anagramas a partir de uma lista de palavras, enquanto que a segunda função cria a tabela de classes de anagramas a partir do referido dicionário.  
🔹 **Exemplo:** `tabela_anagramas(classes_anagramas(["amor", "mora", "ramo", "roma", "galo", "algo", "gola", "ator", "rato", "rota"])` retorna:

| Letras Organizadas | Classes de Anagramas    |
|--------------------|-------------------------|
| aglo               | algo, galo, gola        |
| amor               | amor, mora, ramo, roma  |
| aort               | ator, rato, rota        |

---

## **Menu**

Durante a execução do ficheiro, é exibido um menu com várias opções:
* Testar as funções individualmente, o que requer a introdução de dados por parte do utilizador (opções 1 a 10);
* Executar testes predefinidos, evitando a interação do utilizador (opção 11);
* Sair do programa (opção 0).

